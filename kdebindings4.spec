%bcond_with java
%define kderevision svn961800
 
Name:kdebindings4
Summary: KDE bindings to non-C++ languages
Version: 4.2.85
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
Release: %mkrel 1
Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/kdebindings-%version.tar.bz2
Patch0: kdebindings-4.2.0-nepomuk-allresources.patch
Patch1: kdebindings-4.2.85-t965327-remove-akonadi-private-API.patch
Patch2: kdebindings-4.2.85-t965859-remove-KSystemTimeZones_Simulated.patch
Patch3: kdebindings-4.2.85-t966090-fix-soprano-header-list.patch
Patch4: kdebindings-4.2.85-t966176-add-missing-file.patch
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel
BuildRequires: phonon-devel
BuildRequires: akonadi-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: soprano-devel
BuildRequires: doxygen
%if %with java
BuildRequires: java-devel
%endif # with_java
BuildRequires: ruby-devel
BuildRequires: mono-devel
BuildRequires: python-sip >= 4.7.6
BuildRequires: python-qt4-devel
BuildRequires: qscintilla-qt4-devel
BuildRequires: php-devel
BuildRequires: php-cli
BuildRequires: falcon-devel
BuildRequires: qimageblitz-devel
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
%py_requires -d

%description -n python-kde4
Python KDE 4

%files -n python-kde4
%defattr(-,root,root)
%dir %py_platsitedir/PyKDE4
%py_platsitedir/PyKDE4/*
%_datadir/sip/PyKDE4/*
%_kde_appsdir/pykde4
%_kde_libdir/kde4/krosspython.so
%_kde_libdir/kde4/kpythonpluginfactory.so

#-----------------------------------------------------------------------------

%package -n python-kde4-doc
Summary: PyKDE4 documentation
Group: Development/KDE and Qt

%description -n python-kde4-doc
Python KDE 4 documentation

%files -n python-kde4-doc
%defattr(-,root,root)

#-----------------------------------------------------------------------------

%define lib_smoke_kde_major 2
%define lib_smoke_kde %mklibname smokekde %{lib_smoke_kde_major}

%package -n   %{lib_smoke_kde}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt
Obsoletes:    %{_lib}smokeplasma2 < 4.0.73-1

%description -n %{lib_smoke_kde}
KDE generic bindings library.

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

%files -n %{libsmokeqsci}
%defattr(-,root,root)
%_kde_libdir/libsmokeqsci.so.%{smokeqsci_major}*

#------------------------------------------------------------

%define lib_smokesoprano_major 2
%define lib_smokesoprano %mklibname smokesoprano %{lib_smokesoprano_major}

%package -n %{lib_smokesoprano}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{lib_smokesoprano}
Qt generic bindings library.

%files -n %{lib_smokesoprano}
%defattr(-,root,root)
%_kde_libdir/libsmokesoprano.so.%{lib_smokesoprano_major}*

#------------------------------------------------------------

%define lib_smokeqtscript_major 2
%define lib_smokeqtscript %mklibname smokeqtscript %{lib_smokeqtscript_major}

%package -n %{lib_smokeqtscript}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{lib_smokeqtscript}
Qt generic bindings library.

%files -n %{lib_smokeqtscript}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtscript.so.%{lib_smokeqtscript_major}*

#------------------------------------------------------------
#
#define lib_smokenepomuk_major 
#define lib_smokenepomuk %mklibname smokenepomuk %{lib_smokenepomuk_major}
#
#%package -n %{lib_smokenepomuk}
#Summary: Qt generic bindings library
#Group: Development/KDE and Qt
#
#%description -n %{lib_smokenepomuk}
#Qt generic bindings library.
#
#%files -n %{lib_smokenepomuk}
#%defattr(-,root,root)
#%_kde_libdir/libsmokenepomuk.so.%{lib_smokenepomuk_major}*
#
#------------------------------------------------------------

%define lib_smoke_qt_major 2
%define lib_smoke_qt %mklibname smokeqt %{lib_smoke_qt_major}

%package -n %{lib_smoke_qt}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{lib_smoke_qt}
Qt generic bindings library.

%files -n %{lib_smoke_qt}
%defattr(-,root,root)
%_kde_libdir/libsmokeqt.so.%{lib_smoke_qt_major}*

#------------------------------------------------------------

%define libsmokeplasma_major 2
%define libsmokeplasma %mklibname smokeplasma %{libsmokeplasma_major}

%package -n %{libsmokeplasma}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{libsmokeplasma}
Qt generic bindings library.

%files -n %{libsmokeplasma}
%defattr(-,root,root)
%_kde_libdir/libsmokeplasma.so.%{libsmokeplasma_major}*

#------------------------------------------------------------

%define libsmokenepomuk_major 2
%define libsmokenepomuk %mklibname smokenepomuk %{libsmokenepomuk_major}

%package -n %{libsmokenepomuk}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{libsmokenepomuk}
Qt generic bindings library.

%files -n %{libsmokenepomuk}
%defattr(-,root,root)
%_kde_libdir/libsmokenepomuk.so.%{libsmokenepomuk_major}*

#------------------------------------------------------------

%define libsmokeqttest_major 2
%define libsmokeqttest %mklibname smokeqttest %{libsmokeqttest_major}

%package -n %{libsmokeqttest}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{libsmokeqttest}
Qt generic bindings library.

%files -n %{libsmokeqttest}
%defattr(-,root,root)
%_kde_libdir/libsmokeqttest.so.%{libsmokeqttest_major}*

#------------------------------------------------------------

%define libsmokeakonadi_major 2
%define libsmokeakonadi %mklibname smokeakonadi %{libsmokeakonadi_major}

%package -n %{libsmokeakonadi}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{libsmokeakonadi}
Qt generic bindings library.

%files -n %{libsmokeakonadi}
%defattr(-,root,root)
%_kde_libdir/libsmokeakonadi.so.%{libsmokeakonadi_major}*

#------------------------------------------------------------

%package -n smoke4-devel
Summary: Header files for libsmoke
Group: Development/KDE and Qt
Requires: %{libsmokeplasma} = %epoch:%version-%release
Requires: %{lib_smoke_qt} = %epoch:%version-%release
Requires: %{lib_smoke_kde} = %epoch:%version-%release
Requires: %{libsmokeqsci} = %epoch:%version-%release
#Requires: %{libsmokephonon} = %epoch:%version-%release
#Requires: %{libsmokeokular} = %epoch:%version-%release
Requires: %{libsmokesolid} = %epoch:%version-%release
Requires: %{libsmokeqtwebkit} = %epoch:%version-%release
Requires: %{libsmokeqtuitools} = %epoch:%version-%release
Requires: %{libsmokektexteditor} = %epoch:%version-%release
Requires: %{libsmokekhtml} = %epoch:%version-%release
Requires: %{libsmokeakonadi} = %epoch:%version-%release
Requires: %{libsmokenepomuk} = %epoch:%version-%release
Requires: %{libsmokeqttest} = %epoch:%version-%release
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
Conflicts: qyoto-devel < 1:4.1.73
Conflicts: kimono < 1:4.1.81

%description -n qyoto
C# Mono Qt 4 bindings

%files -n qyoto
%defattr(-,root,root)
%_prefix/lib/mono/2.0/qt-dotnet.dll
%_prefix/lib/mono/2.0/qscintilla.dll
%_prefix/lib/mono/2.0/qtscript.dll
%_prefix/lib/mono/2.0/qtuitools.dll
%_prefix/lib/mono/2.0/qtwebkit.dll
%_prefix/lib/mono/2.0/qttest.dll
%_prefix/lib/mono/gac/qttest
%_prefix/lib/mono/gac/qt-dotnet
%_prefix/lib/mono/gac/qscintilla
%_prefix/lib/mono/gac/qtscript
%_prefix/lib/mono/gac/qtwebkit
%_prefix/lib/mono/gac/qtuitools
%_kde_libdir/libqyoto.so
%_kde_libdir/libqscintilla-sharp.so
%_kde_libdir/libqtscript-sharp.so
%_kde_libdir/libqtuitools-sharp.so
%_kde_libdir/libqtwebkit-sharp.so
%_kde_libdir/libqttest-sharp.so

#------------------------------------------------------------

%package -n phpqt
Summary: PHP KDE 4 bindings
Group: Development/KDE and Qt
Requires: php-cli

%description -n phpqt
PHP KDE 4 bindings

%files -n phpqt
%defattr(-,root,root)
%_kde_bindir/phpuic
%_kde_libdir/php/extensions/php_qt.so

#------------------------------------------------------------

%package -n falcon-kde4
Summary: Falcon KDE 4 bindings
Group: Development/KDE and Qt
Requires: falcon

%description -n falcon-kde4
Falcon KDE 4 bindings

%files -n falcon-kde4
%defattr(-,root,root)
%_kde_libdir/kde4/krossfalcon.so

#------------------------------------------------------------

%package -n kimono
Summary: C# Mono KDE 4 bindings
Group: Development/KDE and Qt
Provides: mono-kde4 = %version-%release
Requires: qyoto = %epoch:%version-%release
Conflicts: ruby-qt4 < 1:4.1.81
Conflicts: qyoto < 1:4.1.81 

%description -n kimono
C# Mono KDE 4 bindings

%files -n kimono
%defattr(-,root,root)
%_prefix/lib/mono/2.0/kde-dotnet.dll
%_prefix/lib/mono/2.0/khtml-dll.dll
%_prefix/lib/mono/2.0/soprano.dll
%_prefix/lib/mono/2.0/akonadi.dll
%_prefix/lib/mono/2.0/ktexteditor-dotnet.dll
%_prefix/lib/mono/2.0/plasma-dll.dll
%_prefix/lib/mono/2.0/nepomuk-dll.dll
%_prefix/lib/mono/gac/kde-dotnet
%_prefix/lib/mono/gac/khtml-dll
%_prefix/lib/mono/gac/soprano
%_prefix/lib/mono/gac/akonadi
%_prefix/lib/mono/gac/ktexteditor-dotnet
%_prefix/lib/mono/gac/plasma-dll
%_prefix/lib/mono/gac/nepomuk-dll
%{_kde_libdir}/kde4/kimonopluginfactory.so
%_kde_libdir/libkhtml-sharp.so
%_kde_libdir/libnepomuk-sharp.so
%_kde_libdir/libsoprano-sharp.so
%_kde_libdir/libkimono.so
%_kde_libdir/libakonadi-sharp.so
%_kde_libdir/libktexteditor-sharp.so
%_kde_libdir/libplasma-sharp.so
%_kde_appsdir/plasma_scriptengine_kimono
%_kde_services/plasma-scriptengine-kimono-applet.desktop
%_kde_services/plasma-scriptengine-kimono-dataengine.desktop

#------------------------------------------------------------

%define libqyotoshared_major 1
%define libqyotoshared %mklibname qyotoshared %{libqyotoshared_major}

%package -n %{libqyotoshared}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{libqyotoshared}
Qt generic bindings library.

%files -n %{libqyotoshared}
%defattr(-,root,root)
%_kde_libdir/libqyotoshared.so.%{libqyotoshared_major}*

#------------------------------------------------------------

%package -n qyoto-devel
Summary: Header files for qyoto
Group: Development/KDE and Qt
Requires: qyoto = %epoch:%version-%release
Requires:  %{libqyotoshared} = %epoch:%version-%release
Conflicts: qyoto < 1:4.1.73

%description -n qyoto-devel
qyoto devel files.

%files -n qyoto-devel
%defattr(-,root,root)
%_kde_bindir/csrcc
%_kde_bindir/uics
%_kde_includedir/qyoto
%_kde_libdir/libqyotoshared.so

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
%ruby_sitearchdir/qscintilla.so
%ruby_sitearchdir/qtruby4.so
%ruby_sitearchdir/qtuitools.so
%ruby_sitearchdir/qtwebkit.so
%ruby_sitearchdir/qtscript.so
%ruby_sitearchdir/qttest.so
%ruby_sitearchdir/akonadi.so
%ruby_sitearchdir/plasma_applet.so
%ruby_sitelibdir/Qt.rb
%ruby_sitelibdir/Qt3.rb
%ruby_sitelibdir/Qt4.rb
%ruby_sitelibdir/Qt
%ruby_sitelibdir/qscintilla
%ruby_sitelibdir/qtuitools
%ruby_sitelibdir/qtwebkit
%ruby_sitelibdir/qtscript
%ruby_sitelibdir/akonadi
%ruby_sitelibdir/qttest

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
%ruby_sitearchdir/khtml.so
%ruby_sitearchdir/korundum4.so
%ruby_sitearchdir/ktexteditor.so
%ruby_sitearchdir/solid.so
%ruby_sitearchdir/soprano.so
#%ruby_sitearchdir/okular.so
%ruby_sitearchdir/nepomuk.so
%ruby_sitelibdir/KDE
%ruby_sitelibdir/khtml
%ruby_sitelibdir/ktexteditor
%ruby_sitelibdir/soprano
%ruby_sitelibdir/nepomuk
%ruby_sitelibdir/solid
#%ruby_sitelibdir/okular

#------------------------------------------------------------

%define libqtruby4shared_major 2
%define libqtruby4shared %mklibname qtruby4shared %{libqtruby4shared_major}

%package -n %{libqtruby4shared}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{libqtruby4shared}
Qt generic bindings library.

%files -n %{libqtruby4shared}
%defattr(-,root,root)
%_kde_libdir/libqtruby4shared.so.%{libqtruby4shared_major}*

#------------------------------------------------------------

%package -n ruby-qt4-devel
Summary: Header files for ruby-qt4
Group: Development/KDE and Qt
Requires: ruby-qt4 = %epoch:%version-%release
Requires: %{libqtruby4shared} = %epoch:%version-%release
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
Requires: ruby-qt4-devel = %epoch:%version-%release

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
%patch0 -p0 -b .akonadi 
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0

%build
# Remove invalid install dir
rm -f csharp/plasma/examples/CMakeLists.txt

%if %with java
export JAVA_HOME=%{java_home}
%endif
%cmake_kde4 \
	%if %with java
	-DENABLE_KROSSJAVA=TRUE \
	%endif
	-DENABLE_PHP-QT=TRUE \
	-DENABLE_QSCINTILLA_SHARP=ON \
	-DENABLE_QSCINTILLA_RUBY=ON \
	-DENABLE_SMOKEKDEVPLATFORM=OFF \
	-DENABLE_KROSSFALCON=ON

%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -fr %buildroot

