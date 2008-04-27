Name: kdebindings4
Summary: K Desktop Environment
Version: 4.0.71
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 1
Source:	ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebindings-%version.tar.bz2
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel
BuildRequires: ruby-devel
BuildRequires: mono-devel
BuildRequires: python-sip >= 4.7.1
BuildRequires: python-qt4-devel
BuildRequires: qscintilla-qt4-devel
%py_requires -d
BuildRoot: %_tmppath/%name-%version-%release-root

%description
Bindings for kde4

#-----------------------------------------------------------------------------

%package -n python-kde4
Summary: PyKDE4 
Group: Development/KDE and Qt
Provides: PyKDE4 = %version-%release
Requires: python-qt4
Requires: python-sip

%description -n python-kde4
Python KDE 4

%files -n python-kde4
%defattr(-,root,root)
%dir %py_platsitedir/PyKDE4
%py_platsitedir/PyKDE4/*
%_datadir/sip/PyKDE4/*
%_kde_appsdir/pykde4
%_kde_libdir/kde4/krosspython.so

#-----------------------------------------------------------------------------

%package -n python-kde4-doc
Summary: PyKDE4 documentation
Group: Development/KDE and Qt

%description -n python-kde4-doc
Python KDE 4 documentation

%files -n python-kde4-doc
%defattr(-,root,root)
%_kde_docdir/*/PyKDE4

#-----------------------------------------------------------------------------

%define lib_smoke_kde %mklibname smokekde 2

%package -n %{lib_smoke_kde}
Summary: KDE generic bindings library
Group: Development/KDE and Qt

%description -n %{lib_smoke_kde}
KDE generic bindings library.

%post -n %{lib_smoke_kde} -p /sbin/ldconfig
%postun -n %{lib_smoke_kde} -p /sbin/ldconfig

%files -n %{lib_smoke_kde}
%defattr(-,root,root)
%_kde_libdir/libsmokekde.so.*

#-----------------------------------------------------------------------------

%define libsmokeplasma %mklibname smokeplasma 2

%package -n %{libsmokeplasma}
Summary: KDE generic bindings library
Group: Development/KDE and Qt

%description -n %{libsmokeplasma}
KDE generic bindings library.

%post -n %{libsmokeplasma} -p /sbin/ldconfig
%postun -n %{libsmokeplasma} -p /sbin/ldconfig

%files -n %{libsmokeplasma}
%defattr(-,root,root)
%_kde_libdir/libsmokeplasma.so.*

#------------------------------------------------------------

%define lib_smoke_qt %mklibname smokeqt 2

%package -n %{lib_smoke_qt}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{lib_smoke_qt}
Qt generic bindings library.

%post -n %{lib_smoke_qt} -p /sbin/ldconfig
%postun -n %{lib_smoke_qt} -p /sbin/ldconfig

%files -n %{lib_smoke_qt}
%defattr(-,root,root)
%_kde_libdir/libsmokeqt.so.*

#------------------------------------------------------------

%package -n smoke4-devel
Summary: Header files for libsmoke
Group: Development/KDE and Qt
Requires: %{lib_smoke_qt} = %epoch:%version-%release
Requires: %{lib_smoke_kde} = %epoch:%version-%release
Provides: libsmoke2-devel = %epoch:%version-%release

%description -n smoke4-devel
Smoke devel files.

%files -n smoke4-devel
%defattr(-,root,root)
%_kde_includedir/smoke.h
%_kde_libdir/libsmokekde.so
%_kde_libdir/libsmokeqt.so
%_kde_libdir/libsmokeplasma.so

#------------------------------------------------------------

%package -n qyoto
Summary: C# Mono KDE 4 bindings
Group: Development/KDE and Qt
Provides: mono-kde4 = %version-%release
Requires: mono

%description -n qyoto
C# Mono KDE 4 bindings

%files -n qyoto
%defattr(-,root,root)
%_kde_bindir/csrcc
%_kde_bindir/uics
%_kde_libdir/libqyoto.so

#------------------------------------------------------------

%define lib_ruby	%mklibname qtruby

%package -n ruby-qt4
Summary: Qt bindings for Ruby
Group:		Development/KDE and Qt
Provides: qtruby = %{epoch}:%{version}-%{release}
Obsoletes: %{lib_ruby} < 3.5.1
Obsoletes: %{lib_ruby}1 < 3.5.1
Obsoletes: %{lib_ruby}1-devel < 3.5.1
Obsoletes: qtruby < 3.5.5

%description -n ruby-qt4
A binding for Ruby language.

%files -n ruby-qt4
%defattr(-,root,root)
%_kde_bindir/rbqtapi
%_kde_bindir/rbrcc
%_kde_bindir/rbuic4
%_kde_bindir/krubyapplication
%_kde_libdir/kde4/krossruby.so
%_kde_libdir/kde4/krubypluginfactory.so
%_prefix/lib/ruby/site_ruby/*/*
%_kde_appsdir/plasma-ruby-webapplet
%_kde_appsdir/plasma-ruby-analog-clock
%_kde_appsdir/plasma-ruby-digital-clock
%_kde_appsdir/plasma-ruby-engine-time
%_kde_appsdir/dbpedia_references
%_kde_datadir/kde4/services/plasma-ruby-applet-web.desktop
%_kde_datadir/kde4/services/plasma-dataengine-dbpedia-albums.desktop
%_kde_datadir/kde4/services/plasma-dataengine-ruby-time.desktop
%_kde_datadir/kde4/services/plasma-ruby-clock-default.desktop
%_kde_datadir/kde4/services/plasma-ruby-digital-clock-default.desktop
%_kde_datadir/applications/kde4/dbpedia_references.desktop

#------------------------------------------------------------

%prep
%setup -q -n kdebindings-%version

%build
%cmake_kde4 

make 


%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

%clean
rm -fr %buildroot

