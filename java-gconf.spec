%define	pname	libgconf-java
Summary:	Java interface for GConf
Summary(pl):	Wrapper Java dla GConf
Name:		java-gconf
Version:	2.8.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.8/%{pname}-%{version}.tar.bz2
# Source0-md5:	58c2af2d9a819eb8d2d8f22330ce45ce
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-CLASSPATH.patch
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.8.0.1
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	gtk+2-devel >= 2:2.4.4
BuildRequires:	java-gtk-devel >= 2.4.5
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
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I `pkg-config --variable macro_dir gtk2-java`
%{__autoconf}
%configure \
	GCJ_JAR=`echo /usr/share/java/libgcj*.jar`

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir},%{_libdir},%{_pkgconfigdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_javadir}/*
%{_pkgconfigdir}/*.pc
