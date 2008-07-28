%define _disable_ld_as_needed 1

%define with_java 0
%{?_with_java: %{expand: %%global with_java 1}}

%define with_php 0
%{?_with_php: %{expand: %%global with_php 1}}

Name:kdebindings4
Summary: KDE bindings to non-C++ languages
Version: 4.1.0
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 2
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebindings-%version.tar.bz2
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel
BuildRequires: phonon-devel
BuildRequires: akonadi-devel
BuildRequires: soprano-devel
BuildRequires: kdebase4-workspace-devel
%if %{with_java}
BuildRequires: java-devel
%endif # with_java
BuildRequires: ruby-devel
BuildRequires: mono-devel
BuildRequires: python-sip >= 4.7.6
BuildRequires: python-qt4-devel
BuildRequires: qscintilla-qt4-devel
%if %{with_php}
BuildRequires: php-devel
BuildRequires: php-cli
%endif # with_php
%py_requires -d

BuildRoot:     %_tmppath/%name-%version-%release-root

%description
KDE4 bindings to non-C++ languages

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
%_kde_docdir/*/*/pykde4

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

%define smokephonon_major 2
%define libsmokephonon %mklibname smokephonon %{smokephonon_major}

%package -n   %{libsmokephonon}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokephonon}
KDE generic bindings library.

%if %mdkversion < 200900
%post -n %{libsmokephonon} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libsmokephonon} -p /sbin/ldconfig
%endif

%files -n %{libsmokephonon}
%defattr(-,root,root)
%_kde_libdir/libsmokephonon.so.%{smokephonon_major}*

#-----------------------------------------------------------------------------

#define #smokesoprano_major 2
#define libsmokesoprano %mklibname smokesoprano %{smokesoprano_major}
#
#%package -n   %{libsmokesoprano}
#Summary:      KDE generic bindings library
#Group:        Development/KDE and Qt
#
#%description -n %{libsmokesoprano}
#KDE generic bindings library.
#
#%if %mdkversion < 200900
#%post -n %{libsmokesoprano} -p /sbin/ldconfig
#%endif
#%if %mdkversion < 200900
#%postun -n %{libsmokesoprano} -p /sbin/ldconfig
#%endif
#
#%files -n %{libsmokesoprano}
#%defattr(-,root,root)
#%_kde_libdir/libsmokesoprano.so.%{smokesoprano_major}*
#
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
Summary: C# Mono Qt 4 bindings
Group: Development/KDE and Qt
Provides: mono-qt4 = %version-%release
Requires: mono
Conflicts: qyoto-devel < 1:4.0.98-2

%description -n qyoto
C# Mono Qt 4 bindings

%files -n qyoto
%defattr(-,root,root)
%_prefix/lib/mono/2.0/qt-dotnet.dll
%_prefix/lib/mono/2.0/qscintilla.dll
%_prefix/lib/mono/gac/qt-dotnet
%_prefix/lib/mono/gac/qscintilla
%_kde_libdir/libqyoto.so
%_kde_libdir/libqyotoshared.so
%_kde_libdir/libqscintilla-sharp.so

#------------------------------------------------------------

%package -n kimono
Summary: C# Mono KDE 4 bindings
Group: Development/KDE and Qt
Provides: mono-kde4 = %version-%release
Requires: qyoto
Requires: mono

%description -n kimono
C# Mono KDE 4 bindings

%files -n kimono
%defattr(-,root,root)
%_prefix/lib/mono/2.0/kde-dotnet.dll
%_prefix/lib/mono/2.0/khtml.dll
%_prefix/lib/mono/gac/kde-dotnet
%_prefix/lib/mono/gac/khtml
%{_kde_libdir}/kde4/kimonopluginfactory.so
%_kde_libdir/libkhtml-sharp.so
%_kde_libdir/libkimono.so

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
%_kde_bindir/csrcc
%_kde_bindir/uics
%_kde_includedir/qyoto

#------------------------------------------------------------

%package -n kimono-devel
Summary: Devel files for kimono
Group: Development/KDE and Qt
Requires: qyoto-devel = %epoch:%version-%release
Requires: kimono = %epoch:%version-%release
Conflicts: qyoto < 1:4.0.80-1

%description -n kimono-devel
kimono devel files.

%files -n kimono-devel
%defattr(-,root,root)

#------------------------------------------------------------

%define lib_ruby	%mklibname qtruby

%package -n ruby-qt4
Summary: Qt bindings for Ruby
Group: Development/KDE and Qt
Provides: qtruby = %{epoch}:%{version}-%{release}
Obsoletes: %{lib_ruby} < 3.5.1
Obsoletes: %{lib_ruby}1 < 3.5.1
Obsoletes: %{lib_ruby}1-devel < 3.5.1
Obsoletes: qtruby < 3.5.5

%description -n ruby-qt4
A qt4 bindings for Ruby language.

%files -n ruby-qt4
%defattr(-,root,root)
%_kde_bindir/rbqtapi
%_kde_libdir/libqtruby4shared.so
%_kde_datadir/applications/kde4/dbpedia_references.desktop
%_kde_appsdir/dbpedia_references
%_prefix/lib/ruby/site_ruby/*/*/qscintilla.so
%_prefix/lib/ruby/site_ruby/*/*/qtruby4.so
%_prefix/lib/ruby/site_ruby/*/*/qtuitools.so
%_prefix/lib/ruby/site_ruby/*/*/qtwebkit.so
%_prefix/lib/ruby/site_ruby/*/Qt.rb
%_prefix/lib/ruby/site_ruby/*/Qt3.rb
%_prefix/lib/ruby/site_ruby/*/Qt4.rb
%_prefix/lib/ruby/site_ruby/*/Qt
%_prefix/lib/ruby/site_ruby/*/qscintilla
%_prefix/lib/ruby/site_ruby/*/qtuitools
%_prefix/lib/ruby/site_ruby/*/qtwebkit

#------------------------------------------------------------

%package -n ruby-kde4
Summary: KDE bindings for Ruby
Group: Development/KDE and Qt
Provides: kderuby = %{epoch}:%{version}-%{release}
Obsoletes: qtruby < 3.5.5
Conflicts: ruby-qt4 < 1:4.0.98-2

%description -n ruby-kde4
A kde4 bindings for Ruby language.

%files -n ruby-kde4
%defattr(-,root,root)
%_kde_bindir/krubyapplication
%_kde_libdir/kde4/krossruby.so
%_kde_libdir/kde4/krubypluginfactory.so
%_prefix/lib/ruby/site_ruby/*/*/khtml.so
%_prefix/lib/ruby/site_ruby/*/*/korundum4.so
%_prefix/lib/ruby/site_ruby/*/*/ktexteditor.so
%_prefix/lib/ruby/site_ruby/*/*/phonon.so
%_prefix/lib/ruby/site_ruby/*/*/solid.so
%_prefix/lib/ruby/site_ruby/*/KDE
%_prefix/lib/ruby/site_ruby/*/khtml
%_prefix/lib/ruby/site_ruby/*/ktexteditor
%_prefix/lib/ruby/site_ruby/*/phonon
%_prefix/lib/ruby/site_ruby/*/solid

#------------------------------------------------------------

%package -n ruby-qt4-devel
Summary: Header files for ruby-qt4
Group: Development/KDE and Qt
Requires: ruby-qt4
Conflicts: ruby-qt4 < 1:4.0.98-2

%description -n ruby-qt4-devel
ruby-qt4 devel files.

%files -n ruby-qt4-devel
%defattr(-,root,root)
%_kde_bindir/rbrcc
%_kde_bindir/rbuic4
%_kde_bindir/rbkconfig_compiler4
%_kde_includedir/qtruby

#------------------------------------------------------------

%package -n ruby-kde4-devel
Summary: Header files for ruby-qt4
Group: Development/KDE and Qt
Requires: ruby-qt4-devel

%description -n ruby-kde4-devel
ruby-qt4 devel files.

%files -n ruby-kde4-devel
%defattr(-,root,root)
%_kde_bindir/rbrcc
%_kde_bindir/rbuic4
%_kde_bindir/rbkconfig_compiler4
%_kde_includedir/qtruby

#------------------------------------------------------------

%prep
%setup -q -n kdebindings-%version

%build
%define _disable_ld_as_needed 1
%cmake_kde4 \
	%if %{with_java}
	-DENABLE_KROSSJAVA=TRUE \
	%endif
	%if %{with_php}
	-DENABLE_PHP-QT=TRUE \
	%endif
	-DENABLE_QSCINTILLA_SHARP=ON \
	-DENABLE_QSCINTILLA_RUBY=ON \
	-DENABLE_SMOKEKDEVPLATFORM=OFF

make


%install
rm -fr %buildroot

make -C build DESTDIR=%buildroot install

%clean
rm -fr %buildroot

