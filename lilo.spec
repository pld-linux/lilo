Summary:	Boot loader for Linux and other operating systems
Summary(de):	Boot-Lader für Linux und andere Betriebssysteme
Summary(es):	Cargador de arranque para Linux y otros sistemas operativos
Summary(fr):	Chargeur de boot pour Linux et autres systèmes d'exploitation
Summary(pl):	Boot Loader dla Linuksa i innych systemów operacyjnych
Summary(pt_BR):	Carregador de boot para Linux e outros sistemas operacionais
Summary(tr):	Linux ve diger iþletim sistemleri için sistem yükleyici
Name:		lilo
Version:	22.2
Release:	2
Epoch:		1
License:	BSD
Group:		Applications/System
Source0:	ftp://brun.dyndns.org/pub/linux/lilo/%{name}-%{version}.tar.gz
Source1:	%{name}-pldblack.bmp
Source2:	%{name}.conf
Source3:	%{name}_functions.sh
Source4:	%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-makefile.patch
#Patch1:		%{name}-cpp-macros.patch
Patch2:		%{name}-evms.patch
BuildRequires:	bin86 >= 0.15
Provides:	bootloader
Exclusivearch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l es
Lilo es responsable de cargar el kernel Linux de un disquete o del
disco duro, dándole el control del sistema. Puede también ser usado
para "bootar" varios otros sistemas operativos, incluyendo variantes
de BSD, DOS y OS/2.

%description -l pl
Lilo jest odpowiedzialny za ³adowanie j±dra systemu Linux z dysku
twardego lub stacji dyskietek. Mo¿e tak¿e byæ u¿ywany do startowania
innych systemów operacyjnych, takich jak ró¿ne warianty BSD czy OS/2,
jak równie¿ DOS.

%description -l pt_BR
Lilo é responsável pelo carregamento do kernel Linux de um disquete ou
do disco rígido, dando a ele o controle do sistema. Ele pode também
ser usado para "bootar" vários outros sistemas operacionais, incluindo
variantes de BSD, DOS e OS/2.

%description -l tr
Lilo, Linux çekirdeðinin disket veya sabit disk sürücüden
yüklenmesinden sorumludur. Ayrýca pek çok diðer iþletim sisteminin de
açýlýþta yüklenmesi için kullanýlýr. Bu sistemler arasýnda BSD
türevleri, DOS ve OS/2 sayýlabilir.

%prep
%setup -q
%patch0 -p1
#%patch1 -p1
%patch2 -p1

%build
%{__make} CC="%{__cc}" OPT="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/sysconfig/rc-boot,%{_mandir}/man{5,8}}

%{__make} install ROOT=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lilo.conf

# driver for rc-boot
install %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/rc-boot

install %{SOURCE1} $RPM_BUILD_ROOT/boot
bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

gzip -9nf README CHANGES INCOMPAT

%clean
rm -rf $RPM_BUILD_ROOT

%post
#if [ -s %{_sysconfdir}/lilo.conf]; then
#	/sbin/lilo
#fi
echo "Remember to type \"lilo\" after upgrade. Or rc-boot if you are using it."

%files
%defattr(644,root,root,755)
%doc *.gz QuickInst
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%{_sysconfdir}/sysconfig/rc-boot/%{name}_functions.sh
%attr(640,root,root) /boot/chain.b
%attr(640,root,root) /boot/os2_d.b
%attr(640,root,root) /boot/boot-*.b
%attr(640,root,root) /boot/mbr.b
%attr(640,root,root) /boot/lilo-pldblack.bmp
%attr(640,root,root) %config(noreplace) %verify(not link) /boot/boot.b
%attr(755,root,root) /sbin/lilo
%{_mandir}/man[58]/*
%lang(cs) %{_mandir}/cs/man[58]/*
%lang(de) %{_mandir}/de/man[58]/*
%lang(es) %{_mandir}/fr/man[58]/*
%lang(hu) %{_mandir}/hu/man[58]/*
%lang(it) %{_mandir}/it/man[58]/*
%lang(ja) %{_mandir}/ja/man[58]/*
%lang(ko) %{_mandir}/ko/man[58]/*
%lang(pl) %{_mandir}/pl/man[58]/*
%lang(ru) %{_mandir}/ru/man[58]/*
