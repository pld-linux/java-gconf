%define	pname	libgconf-java
%define	gtkapi	2.4
Summary:	Java interface for GConf
Summary(pl):	Wrapper Java dla GConf
Name:		java-gconf
Version:	2.5.6
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{pname}/2.5/%{pname}-%{version}.tar.bz2
# Source0-md5:	07fe1b261d0da375b05ca55b2866b0b2
Patch0:		%{name}-configure.patch
Patch1:		%{name}-gconf_cflags.patch
URL:		http://java-gnome.sourceforge.net/
BuildRequires:	GConf2-devel >= 2.5.90
BuildRequires:	autoconf
BuildRequires:	gcc-java >= 3.3.2
BuildRequires:	gtk+2-devel >= 2.3.5
BuildRequires:	java-gtk-devel >= 2.3.6
BuildRequires:	libgcj-devel >= 3.3.2
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
gtkapiversion="%{gtkapi}"; export gtkapiversion
%{__autoconf}
%configure \
	GCJ_JAR=`echo /usr/share/java/libgcj*.jar`
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/java-gnome,%{_libdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_datadir}/java-gnome/*
