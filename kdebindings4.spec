Name:          kdebindings4
Summary:       K Desktop Environment
Version: 4.0.80
Epoch:         1
Group:         Graphical desktop/KDE
License:       GPL
URL:           http://www.kde.org
Release: %mkrel 1
Source:	       ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebindings-%version.tar.bz2
Patch3:        kdebindings-4.0.80-fix-pykde4-build.patch
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel
BuildRequires: ruby-devel
BuildRequires: mono-devel
BuildRequires: python-sip >= 4.7.6
BuildRequires: python-qt4-devel
BuildRequires: qscintilla-qt4-devel
BuildRequires: php-devel
%py_requires -d

BuildRoot:     %_tmppath/%name-%version-%release-root

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

%define lib_smoke_kde_major 2
%define lib_smoke_kde %mklibname smokekde %{lib_smoke_kde_major}

%package -n   %{lib_smoke_kde}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt
Obsoletes:    %{_lib}smokeplasma2 < 4.0.73-1

%description -n %{lib_smoke_kde}
KDE generic bindings library.

%post -n %{lib_smoke_kde} -p /sbin/ldconfig
%postun -n %{lib_smoke_kde} -p /sbin/ldconfig

%files -n %{lib_smoke_kde}
%defattr(-,root,root)
%_kde_libdir/libsmokekde.so.%{lib_smoke_kde_major}*

#-----------------------------------------------------------------------------

%define smokesoprano_major 2
%define libsmokesoprano %mklibname smokesoprano %{smokesoprano_major}

%package -n   %{libsmokesoprano}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt
Obsoletes:    %{_lib}smokeplasma2 < 4.0.73-1

%description -n %{libsmokesoprano}
KDE generic bindings library.

%post -n %{libsmokesoprano} -p /sbin/ldconfig
%postun -n %{libsmokesoprano} -p /sbin/ldconfig

%files -n %{libsmokesoprano}
%defattr(-,root,root)
%_kde_libdir/libsmokesoprano.so.%{smokesoprano_major}*

#-----------------------------------------------------------------------------

%define smokeqsci_major 2
%define libsmokeqsci %mklibname smokeqsci %{smokeqsci_major}

%package -n   %{libsmokeqsci}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt
Obsoletes:    %{_lib}smokeplasma2 < 4.0.73-1

%description -n %{libsmokeqsci}
KDE generic bindings library.

%post -n %{libsmokeqsci} -p /sbin/ldconfig
%postun -n %{libsmokeqsci} -p /sbin/ldconfig

%files -n %{libsmokeqsci}
%defattr(-,root,root)
%_kde_libdir/libsmokeqsci.so.%{smokeqsci_major}*

#------------------------------------------------------------

%define lib_smoke_qt_major 2
%define lib_smoke_qt %mklibname smokeqt %{lib_smoke_qt_major}

%package -n %{lib_smoke_qt}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{lib_smoke_qt}
Qt generic bindings library.

%post -n %{lib_smoke_qt} -p /sbin/ldconfig
%postun -n %{lib_smoke_qt} -p /sbin/ldconfig

%files -n %{lib_smoke_qt}
%defattr(-,root,root)
%_kde_libdir/libsmokeqt.so.%{lib_smoke_qt_major}*

#------------------------------------------------------------

%package -n smoke4-devel
Summary: Header files for libsmoke
Group: Development/KDE and Qt
Requires: %{lib_smoke_qt} = %epoch:%version-%release
Requires: %{lib_smoke_kde} = %epoch:%version-%release
Requires: %{libsmokeqsci} = %epoch:%version-%release
Requires: %{libsmokesoprano} = %epoch:%version-%release
Provides: libsmoke2-devel = %epoch:%version-%release

%description -n smoke4-devel
Smoke devel files.

%files -n smoke4-devel
%defattr(-,root,root)
%_kde_includedir/smoke.h
%_kde_includedir/smoke
%_kde_libdir/libsmokekde.so
%_kde_libdir/libsmokeqt.so
%_kde_libdir/libsmokeqsci.so
%_kde_libdir/libsmokesoprano.so

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

#------------------------------------------------------------

%package -n qyoto-devel
Summary: Header files for qyoto
Group: Development/KDE and Qt
Requires: qyoto = %epoch:%version-%release
Conflicts: qyoto < 1:4.0.80-1
%description -n qyoto-devel
qyoto devel files.

%files -n qyoto-devel
%defattr(-,root,root)
%_kde_libdir/libqyoto.so
%_kde_libdir/libqyotoshared.so
%_kde_includedir/qyoto

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
%_kde_appsdir/dbpedia_references
%_kde_datadir/applications/kde4/dbpedia_references.desktop

#------------------------------------------------------------

%package -n ruby-qt4-devel
Summary: Header files for ruby-qt4
Group: Development/KDE and Qt
Requires: ruby-qt4
%description -n ruby-qt4-devel
ruby-qt4 devel files.

%files -n ruby-qt4-devel
%defattr(-,root,root)
%_kde_includedir/qtruby
%_kde_libdir/libqtruby4shared.so

#------------------------------------------------------------

%prep
%setup -q -n kdebindings-%version
%patch3 -p1

%build
%cmake_kde4  

make


%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

%clean
rm -fr %buildroot

