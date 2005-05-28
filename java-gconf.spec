%define		pname	libgconf-java
Summary:	Java interface for GConf
Summary(pl):	Wrapper Java dla GConf
Name:		java-gconf
Version:	2.10.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.10/%{pname}-%{version}.tar.bz2
# Source0-md5:	73efb6effd65e1fe1b949adb8c70d5db
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.10.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	java-gtk-devel >= 2.6.0
BuildRequires:	libgcj-devel >= 5:3.3.2
BuildRequires:	pkgconfig
Obsoletes:	libgconf-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Java interface for GConf.

%description -l pl
Wrapper Java dla GConf.

%package devel
Summary:	Header files for java-gconf library
Summary(pl):	Pliki nag³ówkowe biblioteki java-gconf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	libgconf-java-devel

%description devel
Header files for java-gconf library.

%description devel -l pl
Pliki nag³ówkowe biblioteki java-gconf.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__aclocal} -I `pkg-config --variable macro_dir gtk2-java`
%{__automake}
%{__autoconf}
%configure \
	GCJ_JAR=`echo %{_datadir}/java/libgcj*.jar` \
	--without-javadocs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir},%{_pkgconfigdir}} \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
mv -f $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}/examples \
        $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/examples/*.in
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{pname}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/lib*-2.10.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%{_examplesdir}/%{name}-%{version}
%{_javadir}/*
%{_pkgconfigdir}/*.pc
