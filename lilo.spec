# TODO:
# - pl-manual is really not-up-to-date
Summary:	Boot loader for Linux and other operating systems
Summary(de.UTF-8):	Boot-Lader für Linux und andere Betriebssysteme
Summary(es.UTF-8):	Cargador de arranque para Linux y otros sistemas operativos
Summary(fr.UTF-8):	Chargeur de boot pour Linux et autres systèmes d'exploitation
Summary(pl.UTF-8):	Boot Loader dla Linuksa i innych systemów operacyjnych
Summary(pt_BR.UTF-8):	Carregador de boot para Linux e outros sistemas operacionais
Summary(ru.UTF-8):	Загрузчик для Linux и других операционных систем
Summary(tr.UTF-8):	Linux ve diger işletim sistemleri için sistem yükleyici
Summary(uk.UTF-8):	Завантажувач для Linux та інших операційних систем
Summary(zh_CN.UTF-8):	Linux 和其它系统的引导模块。
Name:		lilo
Version:	22.8
Release:	1
Epoch:		3
License:	BSD
Group:		Applications/System
Source0:	ftp://metalab.unc.edu/pub/Linux/system/boot/lilo/%{name}-%{version}.src.tar.gz
# Source0-md5:	72765f2aafd20e23ecf07ebd22baeec7
Source1:	%{name}-pldblack.bmp
Source2:	%{name}.conf
Source3:	%{name}_functions.sh
Source4:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source4-md5:	5d93c6c01175d2e701ca77de16368a62
Source5:	%{name}-pldblue.bmp
Source6:	%{name}-pldblue8.bmp
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-nobash.patch
Patch2:		%{name}-cc.patch
Patch3:		%{name}-doc-fallback.patch
Patch4:		%{name}-pagesize.patch
Patch5:		%{name}-dm.patch
Patch6:		%{name}-devmapper.patch
Patch7:		%{name}-degraded_arrary.patch
Patch8:		%{name}-setupspecs.patch
URL:		http://freshmeat.net/projects/lilo/
BuildRequires:	bin86 >= 0.15
BuildRequires:	device-mapper-devel >= 1.01.01
BuildRequires:	sed >= 4.0
Provides:	bootloader
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
Lilo is repsonsible for loading your linux kernel from either a floppy
or a hard drive and giving it control of the system. It can also be
used to boot many other operating sysetms, including the BSD variants,
DOS, and OS/2.

%description -l de.UTF-8
Lilo ist zuständig für das Laden des Linux-Kernels, entweder von einer
Diskette oder einer Festplatte, und übergibt diesem dann die Kontrolle
über das System. Es kann auch benutzt werden, um viele andere
Betriebssysteme zu laden, etwa die BSD-Varianten, DOS und OS/2.

%description -l es.UTF-8
Lilo es responsable de cargar el kernel Linux de un disquete o del
disco duro, dándole el control del sistema. Puede también ser usado
para "bootar" varios otros sistemas operativos, incluyendo variantes
de BSD, DOS y OS/2.

%description -l pl.UTF-8
Lilo jest odpowiedzialny za ładowanie jądra systemu Linux z dysku
twardego lub stacji dyskietek. Może także być używany do startowania
innych systemów operacyjnych, takich jak różne warianty BSD czy OS/2,
jak również DOS.

%description -l pt_BR.UTF-8
Lilo é responsável pelo carregamento do kernel Linux de um disquete ou
do disco rígido, dando a ele o controle do sistema. Ele pode também
ser usado para "bootar" vários outros sistemas operacionais, incluindo
variantes de BSD, DOS e OS/2.

%description -l ru.UTF-8
Lilo отвечает за загрузку ядра Linux с дискеты или жесткого диска и
передачу ему управления системой. Также может быть использовано для
загрузки многих других систем, включая диалекты BSD, DOS и OS/2.

%description -l tr.UTF-8
Lilo, Linux çekirdeğinin disket veya sabit disk sürücüden
yüklenmesinden sorumludur. Ayrıca pek çok diğer işletim sisteminin de
açılışta yüklenmesi için kullanılır. Bu sistemler arasında BSD
türevleri, DOS ve OS/2 sayılabilir.

%description -l uk.UTF-8
Lilo відповідає за завантаження ядра Linux з дискети чи жорсткого
диску та передачі йому керування системою. Дозволяє також
завантажувати інші операційні системи, включаючи діалекти BSD, DOS та
OS/2.

%package -n rc-boot-lilo
Summary:	lilo support for rc-boot
Summary(pl.UTF-8):	Wsparcie lilo dla rc-boot
Group:		Base
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	rc-boot
Provides:	rc-boot-bootloader

%description -n rc-boot-lilo
lilo support for rc-boot.

%description -n rc-boot-lilo -l pl.UTF-8
Wsparcie lilo dla rc-boot.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p2

%build
:> checkit
sed -i -e 's#/bin/bcc#/nonexistant/file#g' Makefile*
%{__make} all \
	CC="%{__cc}" \
	OPT="%{rpmcflags} -DLCF_DEVMAPPER" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/sysconfig/rc-boot,%{_mandir}/man{5,8}}

%{__make} install \
	 ROOT=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lilo.conf

# driver for rc-boot
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/rc-boot

install %{SOURCE1} $RPM_BUILD_ROOT/boot
install %{SOURCE5} $RPM_BUILD_ROOT/boot
install %{SOURCE6} $RPM_BUILD_ROOT/boot

touch $RPM_BUILD_ROOT%{_sysconfdir}/disktab

bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo "Remember to type \"lilo\" after upgrade. Or rc-boot if you are using it."

%files
%defattr(644,root,root,755)
%doc README* CHANGES INCOMPAT QuickInst
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(600,root,root) %config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/disktab
/boot/diag1.img
/boot/lilo-pldblack.bmp
/boot/lilo-pldblue.bmp
/boot/lilo-pldblue8.bmp
%attr(755,root,root) %{_sbindir}/lilo
%attr(755,root,root) %{_sbindir}/mkrescue
%{_mandir}/man[58]/*
%lang(cs) %{_mandir}/cs/man[58]/*
%lang(de) %{_mandir}/de/man[58]/*
%lang(es) %{_mandir}/es/man[58]/*
%lang(fr) %{_mandir}/fr/man[58]/*
%lang(hu) %{_mandir}/hu/man[58]/*
%lang(it) %{_mandir}/it/man[58]/*
%lang(ja) %{_mandir}/ja/man[58]/*
%lang(ko) %{_mandir}/ko/man[58]/*
%lang(pl) %{_mandir}/pl/man[58]/*
%lang(ru) %{_mandir}/ru/man[58]/*

%files -n rc-boot-lilo
%defattr(644,root,root,755)
/etc/sysconfig/rc-boot/%{name}_functions.sh
