%define		pname	libgconf-java
Summary:	Java interface for GConf
Summary(pl.UTF-8):	Wrapper Javy dla GConfa
Name:		java-gconf
Version:	2.12.6
Release:	3
License:	LGPL
Group:		Libraries/Java
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libgconf-java/2.12/%{pname}-%{version}.tar.bz2
# Source0-md5:	9e7081679c31abf946c2071fe8ca1895
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.16.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gcc-java >= 5:3.3.2
BuildRequires:	java-gtk-devel >= 2.10.2
BuildRequires:	libgcj-devel >= 5:3.3.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
Obsoletes:	libgconf-java
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		macros  %{_datadir}/glib-java/macros

%description
Java interface for GConf.

%description -l pl.UTF-8
Wrapper Javy dla GConfa.

%package devel
Summary:	Header files for java-gconf library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki java-gconf
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	java-gtk-devel >= 2.10.2
Obsoletes:	libgconf-java-devel

%description devel
Header files for java-gconf library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki java-gconf.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I `pkg-config --variable macro_dir gtk2-java` -I %{macros}
%{__automake}
%{__autoconf}
%configure \
	GCJFLAGS="%{rpmcflags}" \
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
%attr(755,root,root) %{_libdir}/lib*-2.12.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%{_examplesdir}/%{name}-%{version}
%{_javadir}/*
%{_pkgconfigdir}/*.pc
