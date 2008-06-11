%define with_ruby 0
%{?_with_ruby: %{expand: %%global with_ruby 1}}

Name:kdebindings4
Summary: K Desktop Environment
Version: 4.0.82
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebindings-%version.tar.bz2
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel
%if %{with_ruby}
BuildRequires: ruby-devel
%endif # with_ruby
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

%if %mdkversion < 200900
%post -n %{lib_smoke_kde} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_smoke_kde} -p /sbin/ldconfig
%endif

%files -n %{lib_smoke_kde}
%defattr(-,root,root)
%_kde_libdir/libsmokekde.so.%{lib_smoke_kde_major}*

#-----------------------------------------------------------------------------

%define smokekhtml_major 2
%define libsmokekhtml %mklibname smokekhtml %{smokekhtml_major}

%package -n   %{libsmokekhtml}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokekhtml}
KDE generic bindings library.

%if %mdkversion < 200900
%post -n %{libsmokekhtml} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libsmokekhtml} -p /sbin/ldconfig
%endif

%files -n %{libsmokekhtml}
%defattr(-,root,root)
%_kde_libdir/libsmokekhtml.so.%{smokekhtml_major}*

#-----------------------------------------------------------------------------

%define smokektexteditor_major 2
%define libsmokektexteditor %mklibname smoketexteditor %{smokektexteditor_major}

%package -n   %{libsmokektexteditor}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokektexteditor}
KDE generic bindings library.

%if %mdkversion < 200900
%post -n %{libsmokektexteditor} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libsmokektexteditor} -p /sbin/ldconfig
%endif

%files -n %{libsmokektexteditor}
%defattr(-,root,root)
%_kde_libdir/libsmokektexteditor.so.%{smokektexteditor_major}*

#-----------------------------------------------------------------------------

%define smokeqtuitools_major 2
%define libsmokeqtuitools %mklibname smokeqtuitools %{smokeqtuitools_major}

%package -n   %{libsmokeqtuitools}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtuitools}
KDE generic bindings library.

%if %mdkversion < 200900
%post -n %{libsmokeqtuitools} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libsmokeqtuitools} -p /sbin/ldconfig
%endif

%files -n %{libsmokeqtuitools}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtuitools.so.%{smokeqtuitools_major}*

#-----------------------------------------------------------------------------

%define smokeqtwebkit_major 2
%define libsmokeqtwebkit %mklibname smokeqtwebkit %{smokeqtwebkit_major}

%package -n   %{libsmokeqtwebkit}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtwebkit}
KDE generic bindings library.

%if %mdkversion < 200900
%post -n %{libsmokeqtwebkit} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libsmokeqtwebkit} -p /sbin/ldconfig
%endif

%files -n %{libsmokeqtwebkit}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtwebkit.so.%{smokeqtwebkit_major}*

#-----------------------------------------------------------------------------

%define smokesolid_major 2
%define libsmokesolid %mklibname smokesolid %{smokesolid_major}

%package -n   %{libsmokesolid}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokesolid}
KDE generic bindings library.

%if %mdkversion < 200900
%post -n %{libsmokesolid} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libsmokesolid} -p /sbin/ldconfig
%endif

%files -n %{libsmokesolid}
%defattr(-,root,root)
%_kde_libdir/libsmokesolid.so.%{smokesolid_major}*

#-----------------------------------------------------------------------------

%define smokeqsci_major 2
%define libsmokeqsci %mklibname smokeqsci %{smokeqsci_major}

%package -n   %{libsmokeqsci}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt
Obsoletes:    %{_lib}smokeplasma2 < 4.0.73-1

%description -n %{libsmokeqsci}
KDE generic bindings library.

%if %mdkversion < 200900
%post -n %{libsmokeqsci} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libsmokeqsci} -p /sbin/ldconfig
%endif

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

%if %mdkversion < 200900
%post -n %{lib_smoke_qt} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_smoke_qt} -p /sbin/ldconfig
%endif

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
Requires: %{libsmokesolid} = %epoch:%version-%release
Requires: %{libsmokeqtwebkit} = %epoch:%version-%release
Requires: %{libsmokeqtuitools} = %epoch:%version-%release
Requires: %{libsmokektexteditor} = %epoch:%version-%release
Requires: %{libsmokekhtml} = %epoch:%version-%release
Provides: libsmoke2-devel = %epoch:%version-%release

%description -n smoke4-devel
Smoke devel files.

%files -n smoke4-devel
%defattr(-,root,root)
%_kde_includedir/smoke.h
%_kde_includedir/smoke
%_kde_libdir/libsmoke*.so

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
%_kde_libdir/libqscintilla-sharp.so
%_kde_includedir/qyoto

#------------------------------------------------------------
%if %{with_ruby}

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

%endif # with_ruby

#------------------------------------------------------------

%prep
%setup -q -n kdebindings-%version

%build
%cmake_kde4 \
	%if ! %{with_ruby}
	-DBUILD_ruby=FALSE \
	%endif
	-DENABLE_PHP-QT=ON \
	-DENABLE_QSCINTILLA_SHARP=ON \
	-DENABLE_SMOKEQSCI=ON

make


%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

%clean
rm -fr %buildroot

