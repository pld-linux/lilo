Summary:	Boot loader for Linux and other operating systems
Summary(de):	Boot-Lader für Linux und andere Betriebssysteme
Summary(fr):	Chargeur de boot pour Linux et autres systèmes d'exploitation
Summary(pl):	Boot Loader dla Linuxa i innych systemów operacyjnych
Summary(tr):	Linux ve diger iþletim sistemleri için sistem yükleyici
Name:		lilo
Version:	21.4.3
Release:	1
License:	MIT
Group:		Utilities/System 
Group(pl):	Narzêdzia/System 
Source0:	ftp://sd.dynhost.com/pub/linux/lilo/%{name}-%{version}.tar.gz
Source1:	lilo.8
Source2:	lilo.conf.5
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

%description -l pl
Lilo jest odpowiedzialny za ³adowanie j±dra systemu Linux z dysku twardego
lub stacji dyskietek. Mo¿e tak¿e byæ u¿ywany do startowania innych systemów
operacyjnych, takich jak ró¿ne warianty BSD czy OS/2, jak równie¿ DOS.

%description -l tr
Lilo, Linux çekirdeðinin disket veya sabit disk sürücüden yüklenmesinden
sorumludur. Ayrýca pek çok diðer iþletim sisteminin de açýlýþta yüklenmesi
için kullanýlýr. Bu sistemler arasýnda BSD türevleri, DOS ve OS/2 sayýlabilir.

%prep
%setup -q

%build
%{__make} OPTIMIZE="$RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc,%{_mandir}/man{5,8}}

%{__make} install ROOT=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/etc/lilo.conf

install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/man5

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[58]/* \
	README CHANGES INCOMPAT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES,INCOMPAT}.gz QuickInst

%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) /etc/*
%attr(640,root,root) /boot/*.b
%attr(755,root,root) /sbin/lilo
%{_mandir}/man[58]/*
