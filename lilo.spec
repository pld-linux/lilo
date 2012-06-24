Summary:	Boot loader for Linux and other operating systems
Summary(de):	Boot-Lader f�r Linux und andere Betriebssysteme
Summary(fr):	Chargeur de boot pour Linux et autres syst�mes d'exploitation
Summary(pl):	Boot Loader dla Linuxa i innych system�w operacyjnych
Summary(tr):	Linux ve diger i�letim sistemleri i�in sistem y�kleyici
Name:		lilo
Version:	22.0
Release:	1
Epoch:		1
License:	MIT
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://brun.dyndns.org/pub/linux/lilo/beta/%{name}-%{version}-beta.tar.gz
Source1:	%{name}-pldblack.bmp
Source2:	%{name}.conf
Patch0:		%{name}-makefile.patch
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
Lilo ist zust�ndig f�r das Laden des Linux-Kernels, entweder von einer
Diskette oder einer Festplatte, und �bergibt diesem dann die Kontrolle
�ber das System. Es kann auch benutzt werden, um viele andere
Betriebssysteme zu laden, etwa die BSD-Varianten, DOS und OS/2.

%description -l pl
Lilo jest odpowiedzialny za �adowanie j�dra systemu Linux z dysku
twardego lub stacji dyskietek. Mo�e tak�e by� u�ywany do startowania
innych system�w operacyjnych, takich jak r�ne warianty BSD czy OS/2,
jak r�wnie� DOS.

%description -l tr
Lilo, Linux �ekirde�inin disket veya sabit disk s�r�c�den
y�klenmesinden sorumludur. Ayr�ca pek �ok di�er i�letim sisteminin de
a��l��ta y�klenmesi i�in kullan�l�r. Bu sistemler aras�nda BSD
t�revleri, DOS ve OS/2 say�labilir.

%prep
%setup -q -n %{name}-%{version}-beta
%patch0 -p1

%build
%{__make} OPTIMIZE="%{rpmcflags}" LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man{5,8}}

%{__make} install ROOT=$RPM_BUILD_ROOT

#touch $RPM_BUILD_ROOT%{_sysconfdir}/lilo.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/lilo.conf

install %{SOURCE1} $RPM_BUILD_ROOT/boot

gzip -9nf README CHANGES INCOMPAT

%post
#if [ -s %{_sysconfdir}/lilo.conf]; then
#	/sbin/lilo
#fi
[ ! -r /etc/sysconfig/rc-boot/lilo_functions.sh ] || ln -sf /etc/sysconfig/rc-boot/lilo_functions.sh /etc/sysconfig/rc-boot/functions.sh
echo "Remember to type \"lilo\" after upgrade. Or rc-boot if you are using it."


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz QuickInst
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/*
%attr(640,root,root) /boot/chain.b
%attr(640,root,root) /boot/os2_d.b
%attr(640,root,root) /boot/boot-*.b
%attr(640,root,root) /boot/mbr.b
%attr(640,root,root) /boot/lilo-pldblack.bmp
%attr(640,root,root) %config(noreplace) %verify(not link) /boot/boot.b
%attr(755,root,root) /sbin/lilo
%{_mandir}/man[58]/*
