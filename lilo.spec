Summary:	Boot loader for Linux and other operating systems
Summary(de):	Boot-Lader f�r Linux und andere Betriebssysteme
Summary(es):	Cargador de arranque para Linux y otros sistemas operativos
Summary(fr):	Chargeur de boot pour Linux et autres syst�mes d'exploitation
Summary(pl):	Boot Loader dla Linuksa i innych system�w operacyjnych
Summary(pt_BR):	Carregador de boot para Linux e outros sistemas operacionais
Summary(ru):	��������� ��� Linux � ������ ������������ ������
Summary(tr):	Linux ve diger i�letim sistemleri i�in sistem y�kleyici
Summary(uk):	������������ ��� Linux �� ����� �����æ���� ������
Summary(zh_CN):	Linux ������ϵͳ������ģ�顣
Name:		lilo
Version:	22.7
Release:	2
Epoch:		2
License:	BSD
Group:		Applications/System
Source0:	http://home.san.rr.com/johninsd/pub/linux/lilo/%{name}-%{version}.src.tar.gz
# Source0-md5:	565cda4cd5e7c740403ed91e0bdf15f6
Source1:	%{name}-pldblack.bmp
Source2:	%{name}.conf
Source3:	%{name}_functions.sh
Source4:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source4-md5:	5d93c6c01175d2e701ca77de16368a62
Source5:	%{name}-pldblue.bmp
Source6:	%{name}-pldblue8.bmp
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-nobash.patch
Patch2:		%{name}-ioctls.patch
Patch3:		%{name}-cc.patch
Patch4:		%{name}-doc-fallback.patch
Patch5:		%{name}-pagesize.patch
URL:		http://home.san.rr.com/johninsd/pub/linux/lilo/
BuildRequires:	bin86 >= 0.15
Provides:	bootloader
ExclusiveArch:	%{ix86} %{x8664}
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

%description -l es
Lilo es responsable de cargar el kernel Linux de un disquete o del
disco duro, d�ndole el control del sistema. Puede tambi�n ser usado
para "bootar" varios otros sistemas operativos, incluyendo variantes
de BSD, DOS y OS/2.

%description -l pl
Lilo jest odpowiedzialny za �adowanie j�dra systemu Linux z dysku
twardego lub stacji dyskietek. Mo�e tak�e by� u�ywany do startowania
innych system�w operacyjnych, takich jak r�ne warianty BSD czy OS/2,
jak r�wnie� DOS.

%description -l pt_BR
Lilo � respons�vel pelo carregamento do kernel Linux de um disquete ou
do disco r�gido, dando a ele o controle do sistema. Ele pode tamb�m
ser usado para "bootar" v�rios outros sistemas operacionais, incluindo
variantes de BSD, DOS e OS/2.

%description -l ru
Lilo �������� �� �������� ���� Linux � ������� ��� �������� ����� �
�������� ��� ���������� ��������. ����� ����� ���� ������������ ���
�������� ������ ������ ������, ������� �������� BSD, DOS � OS/2.

%description -l tr
Lilo, Linux �ekirde�inin disket veya sabit disk s�r�c�den
y�klenmesinden sorumludur. Ayr�ca pek �ok di�er i�letim sisteminin de
a��l��ta y�klenmesi i�in kullan�l�r. Bu sistemler aras�nda BSD
t�revleri, DOS ve OS/2 say�labilir.

%description -l uk
Lilo צ���צ��� �� ������������ ���� Linux � ������� �� ���������
����� �� ������ަ ���� ��������� ��������. ������Ѥ �����
������������� ��ۦ �����æ�Φ �������, ��������� Ħ������ BSD, DOS ��
OS/2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
sed -i -e 's#/usr/bin/bcc#/nonexistant/file#g' Makefile*
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}" \
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
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}.conf
%attr(600,root,root) %config(noreplace,missingok) %verify(not size mtime md5) %{_sysconfdir}/disktab
/etc/sysconfig/rc-boot/%{name}_functions.sh
/boot/diag1.img
/boot/lilo-pldblack.bmp
/boot/lilo-pldblue.bmp
/boot/lilo-pldblue8.bmp
%attr(755,root,root) /sbin/lilo
%attr(755,root,root) /sbin/mkrescue
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
