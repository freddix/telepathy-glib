Summary:	Telepathy Glib bindings
Name:		telepathy-glib
Version:	0.24.0
Release:	2
License:	LGPL v2
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-glib/%{name}-%{version}.tar.gz
# Source0-md5:	93c429e37750b25dcf8de86bb514664f
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	glib-gio-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkg-config
BuildRequires:	vala-vapigen
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telepathy Glib bindings.

%package devel
Summary:	Header files for telepathy-glib library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for telepathy
library.

%package apidocs
Summary:	telepathy-glib API documentation
Group:		Development/Libraries
Requires:	gtk-doc-common

%description apidocs
telepathy-glib API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--enable-static=no	\
	--enable-vala-bindings	\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/telepathy

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%dir %{_libdir}/telepathy
%attr(755,root,root) %ghost %{_libdir}/libtelepathy-glib.so.?
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%{_includedir}/telepathy-*
%attr(755,root,root) %{_libdir}/libtelepathy-glib.so
%{_pkgconfigdir}/telepathy-glib.pc
%{_datadir}/gir-1.0/TelepathyGLib-0.12.gir
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/telepathy-glib

