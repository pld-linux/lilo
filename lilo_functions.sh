# rc-boot driver for lilo

LOADER_CONFIG=/etc/lilo.conf

rc_boot_prep_image () {
  if [ "$GRUB_ONLY" != "" ] && is_yes "$GRUB_ONLY" ; then 
    return 0
  fi
}

rc_boot_init () {
  if test -z "$LILO_MENU_COLORS" ; then
    LILO_MENU_COLORS=wk:kc:ck:Ck
  fi
  if test -z "$LILO_MENU_TITLE" ; then
    LILO_MENU_TITLE="PLD Linux"
  fi
  
  # This is the main part of the /etc/lilo.conf
  cat <<!EOF!
# By default boot the $DEFAULT entry
default=${DEFAULT}
# Wait ${TIMEOUT} seconds for booting
timeout=${TIMEOUT}0
# Default bootpartition
boot=${BOOT}
# well, we want to be asked...
prompt
# menu stuff ;)
menu-title = "$LILO_MENU_TITLE"
menu-scheme = "$LILO_MENU_COLORS"
read-only
# additional:
!EOF!
  
  if test "$LILO_BMP" ; then
    echo "# bitmap!"
    echo "install = /boot/boot-bmp.b"
    echo "bitmap = $LILO_BMP"
    echo "bmp-colors = $LILO_BMP_COLORS"
    echo "bmp-table = $LILO_BMP_TABLE"
    echo "bmp-timer = $LILO_BMP_TIMER"
    echo "# flags:"
  fi

 
  if is_yes "$LBA32" ; then
    echo "lba32"
  fi

  if test "$PASSWORD" ; then
    echo "password = $PASSWORD"
    echo "restricted"
  fi
}

rc_boot_image () {
  if [ "$GRUB_ONLY" != "" ] && is_yes "$GRUB_ONLY" ; then 
    return 0
  fi
  
  case "$TYPE" in
    linux)  # This is Linux. Lets make an entry 
            # for this in /etc/lilo.conf
      echo "# Linux image"
      echo "image=${KERNEL}"
      echo "   label=${NAME}"
      echo "   root=${ROOT}"
      [ "${VGA}" != "" ] 	&& echo "   vga=${VGA}"
      [ "${APPEND}" != "" ] 	&& echo "   append=\"${APPEND}\""
      [ "$INITRD" != "" ] 	&& echo "   initrd=${INITRD}"
      if is_yes "$LOCK" && test "$PASSWORD" ; then
        echo "    password = $PASSWORD"
      fi
      ;;
    bsd | dos)
      echo "# $TYPE image"
      echo "other=${ROOT}"
      echo "   label=${NAME}"
      if is_yes "$LOCK" && test "$PASSWORD" ; then
        echo "    password = $PASSWORD"
      fi
      ;;
    *)	# Buuu 
      die "Don't know how to handle OS type = '$TYPE'"
      ;;
  esac
}

rc_boot_fini () {
  echo "# EOF"
}


rc_boot_run () {
  lilo >/dev/null 2>&1
}

# Thats all folk.
