Summary:     Boot loader for Linux and other operating systems
Summary(de): Boot-Lader für Linux und andere Betriebssysteme
Summary(fr): Chargeur de boot pour Linux et autres systèmes d'exploitation
Summary(pl): Boot Loader dla Linuxa i innych systemów operacyjnych.
Summary(tr): Linux ve diger iþletim sistemleri için sistem yükleyici
Name:        lilo
Version:     0.20
Release:     4
Copyright:   MIT
Group:       Utilities/System 
Source0:     ftp://sunsite.unc.edu/pub/Linux/system/boot/lilo/%{name}-20.tar.gz
Source1:     lilo.8
Source2:     lilo.conf.5
Exclusivearch: i386
Buildroot:   /tmp/%{name}-%{version}-root

%description
Lilo is repsonsible for loading your linux kernel from either a floppy
or a hard drive and giving it control of the system. It can also be
used to boot many other operating sysetms, including the BSD variants,
DOS, and OS/2.

%description -l de
Lilo ist zuständig für das Laden des Linux-Kernels, entweder von einer
Diskette oder einer Festplatte, und übergibt diesem dann die Kontrolle
über das System. Es kann auch benutzt werden, um viele andere
Betriebssysteme zu laden, etwa die BSD-Varianten, DOS und OS/2.

%description -l pl
Lilo jest odpowiedzialny za ³adowanie j±dra systemu Linux z dysku twardego
lub stacji dyskietek. Mo¿e tak¿e byæ u¿ywany do startowania innych systemów
operacyjnych, takich jak ró¿ne warianty BSD czy OS/2, jak równie¿ DOS.

%description -l tr
Lilo, Linux çekirdeðinin disket veya sabit disk sürücüden yüklenmesinden
sorumludur. Ayrýca pek çok diðer iþletim sisteminin de açýlýþta yüklenmesi
için kullanýlýr. Bu sistemler arasýnda BSD türevleri, DOS ve OS/2 sayýlabilir.

%prep
%setup -q -n %{name}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,usr/man/man{5,8}}

make install ROOT=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/etc/lilo.conf

install %{SOURCE1} $RPM_BUILD_ROOT/usr/man/man8
install %{SOURCE2} $RPM_BUILD_ROOT/usr/man/man5

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/lilo > /dev/null

%files
%defattr(644, root, root,755)
%doc README CHANGES INCOMPAT QuickInst
%attr(640, root, root) %config(noreplace) %verify(not size mtime md5) /etc/*
%attr(640, root, root) /boot/*.b
%attr(750, root, root) /sbin/lilo
%attr(644, root,  man) /usr/man/man[58]/*

%changelog
* Sat Dec  7 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.20-4]
- removed doc/* from %doc,
- added lilo(8) and lilo.conf(5) man pages (moved from man-pages
  package).

* Sun Nov  8 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.20-3]
- changed permission of lilo to 750,
- removed doc/* from %doc,

* Mon Jun 15 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added pl translation,
- changed permission of lilo to 711,
- moved %changelog at the end of spec.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to release 0.20
- uses a build root

* Tue Jul 08 1997 Erik Troan <ewt@redhat.com>
- built against glibc
