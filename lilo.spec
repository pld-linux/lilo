Summary:	Boot loader for Linux and other operating systems
Summary(de):	Boot-Lader für Linux und andere Betriebssysteme
Summary(fr):	Chargeur de boot pour Linux et autres systèmes d'exploitation
Summary(pl):	Boot Loader dla Linuxa i innych systemów operacyjnych
Summary(tr):	Linux ve diger iþletim sistemleri için sistem yükleyici
Name:		lilo
Version:	0.21
Release:	4
Copyright:	MIT
Group:		Utilities/System 
Group(pl):	Narzêdzia/System 
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/boot/lilo/%{name}-21.tar.gz
Source1:	lilo.8
Source2:	lilo.conf.5
Exclusivearch:	i386
Buildroot:	/tmp/%{name}-%{version}-root

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
make OPTIMIZE="$RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc,usr/man/man{5,8}}

make install ROOT=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/etc/lilo.conf

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man5

gzip -9nf README CHANGES INCOMPAT
gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[58]/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/lilo > /dev/null

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,INCOMPAT}.gz2 QuickInst

%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) /etc/*
%attr(640,root,root) /boot/*.b
%attr(755,root,root) /sbin/lilo
%{_mandir}/man[58]/*

%changelog
* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [0.21-4]
- gzipping instead bzipping

* Wed Mar 12 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.21-3]
- do not compress QuickInst,
- removed man group from man pages.

* Sat Mar 06 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
- added Group(pl),
- commpressed man pages && documentation (QuickInst script too ..),
- fixed permissions,
- build with optimization,
- cleaning up spec.

* Fri Mar 5 1999 Jacek Smyda <smyda@posexperts.com.pl>
- change permission for lilo.conf

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
- moved %changelog at the end of spec,
- build against GNU libc-2.1,
- start at RH spec.
