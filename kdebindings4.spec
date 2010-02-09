%bcond_with java 0
%bcond_with falcon 0

%define branch 0
%{?_branch: %{expand: %%global branch 1}}


%if %branch
%define kde_snapshot svn1053190
%endif

Name:kdebindings4
Summary: KDE bindings to non-C++ languages
Version: 4.4.0
Release: %mkrel 2
Epoch: 1
Group: Graphical desktop/KDE
License: GPL
URL: http://www.kde.org
%if %branch
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdebindings-%version%kde_snapshot.tar.bz2
%else
Source: ftp://ftp.kde.org/pub/kde/unstable/%version/src/kdebindings-%version.tar.bz2
%endif
BuildRequires: kde4-macros
BuildRequires: cmake
BuildRequires: kdelibs4-devel >= 2:4.3.85
BuildRequires: phonon-devel
BuildRequires: akonadi-devel
BuildRequires: kdepimlibs4-devel >= 2:4.3.85
BuildRequires: kdegraphics4-devel
BuildRequires: qimageblitz-devel
BuildRequires: soprano-devel
BuildRequires: doxygen
BuildRequires: java-devel
BuildRequires: ruby-devel
%ifnarch %arm %mips
BuildRequires: mono-devel
%endif
BuildRequires: python-sip >= 4.7.6
BuildRequires: python-qt4-devel >= 4.5.1
BuildRequires: qscintilla-qt4-devel
BuildRequires: php-devel
BuildRequires: php-cli
BuildRequires: polkit-qt-devel
%if %with falcon
BuildRequires: falcon-devel
%endif
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
%py_platsitedir/PyQt4/*
%py_platsitedir/PyKDE4/*
%_datadir/sip/PyKDE4/*
%_kde_bindir/pykdeuic4
%_kde_libdir/kde4/krosspython.so
%_kde_libdir/kde4/kpythonpluginfactory.so
%_kde_appsdir/pykde4

%pre -n python-kde4
rm -rf %_bindir/pykdeuic4

#-----------------------------------------------------------------------------

%package -n python-kde4-doc
Summary: PyKDE4 documentation
Group: Development/KDE and Qt

%description -n python-kde4-doc
Python KDE 4 documentation

%files -n python-kde4-doc
%defattr(-,root,root)
%_datadir/doc/python-kde4

#-----------------------------------------------------------------------------

%define smokeqtcore_major 3
%define libsmokeqtcore %mklibname smokeqtcore %{smokeqtcore_major}

%package -n   %{libsmokeqtcore}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtcore}
KDE generic bindings library.

%files -n %{libsmokeqtcore}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtcore.so.%{smokeqtcore_major}*

#-----------------------------------------------------------------------------

%define smokeqtdbus_major 3
%define libsmokeqtdbus %mklibname smokeqtdbus %{smokeqtdbus_major}

%package -n   %{libsmokeqtdbus}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtdbus}
KDE generic bindings library.

%files -n %{libsmokeqtdbus}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtdbus.so.%{smokeqtdbus_major}*

#-----------------------------------------------------------------------------

%define smokeqtgui_major 3
%define libsmokeqtgui %mklibname smokeqtgui %{smokeqtgui_major}

%package -n   %{libsmokeqtgui}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtgui}
KDE generic bindings library.

%files -n %{libsmokeqtgui}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtgui.so.%{smokeqtgui_major}*

#-----------------------------------------------------------------------------

%define smokeqtmultimedia_major 3
%define libsmokeqtmultimedia %mklibname smokeqtmultimedia %{smokeqtmultimedia_major}

%package -n   %{libsmokeqtmultimedia}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtmultimedia}
KDE generic bindings library.

%files -n %{libsmokeqtmultimedia}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtmultimedia.so.%{smokeqtmultimedia_major}*

#-----------------------------------------------------------------------------

%define smokeqtnetwork_major 3
%define libsmokeqtnetwork %mklibname smokeqtnetwork %{smokeqtnetwork_major}

%package -n   %{libsmokeqtnetwork}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtnetwork}
KDE generic bindings library.

%files -n %{libsmokeqtnetwork}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtnetwork.so.%{smokeqtnetwork_major}*

#-----------------------------------------------------------------------------

%define smokeqtopengl_major 3
%define libsmokeqtopengl %mklibname smokeqtopengl %{smokeqtopengl_major}

%package -n   %{libsmokeqtopengl}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtopengl}
KDE generic bindings library.

%files -n %{libsmokeqtopengl}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtopengl.so.%{smokeqtopengl_major}*

#-----------------------------------------------------------------------------

%define smokeqtsql_major 3
%define libsmokeqtsql %mklibname smokeqtsql %{smokeqtsql_major}

%package -n   %{libsmokeqtsql}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtsql}
KDE generic bindings library.

%files -n %{libsmokeqtsql}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtsql.so.%{smokeqtsql_major}*

#-----------------------------------------------------------------------------

%define smokeqtsvg_major 3
%define libsmokeqtsvg %mklibname smokeqtsvg %{smokeqtsvg_major}

%package -n   %{libsmokeqtsvg}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtsvg}
KDE generic bindings library.

%files -n %{libsmokeqtsvg}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtsvg.so.%{smokeqtsvg_major}*

#-----------------------------------------------------------------------------

%define smokeqtxml_major 3
%define libsmokeqtxml %mklibname smokeqtxml %{smokeqtxml_major}

%package -n   %{libsmokeqtxml}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtxml}
KDE generic bindings library.

%files -n %{libsmokeqtxml}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtxml.so.%{smokeqtxml_major}*

#-----------------------------------------------------------------------------

%define smokeqtxmlpatterns_major 3
%define libsmokeqtxmlpatterns %mklibname smokeqtxmlpatterns %{smokeqtxmlpatterns_major}

%package -n   %{libsmokeqtxmlpatterns}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqtxmlpatterns}
KDE generic bindings library.

%files -n %{libsmokeqtxmlpatterns}
%defattr(-,root,root)
%_kde_libdir/libsmokeqtxmlpatterns.so.%{smokeqtxmlpatterns_major}*

#-----------------------------------------------------------------------------

%define smokesopranoclient_major 3
%define libsmokesopranoclient %mklibname smokesopranoclient %{smokesopranoclient_major}

%package -n   %{libsmokesopranoclient}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokesopranoclient}
KDE generic bindings library.

%files -n %{libsmokesopranoclient}
%defattr(-,root,root)
%_kde_libdir/libsmokesopranoclient.so.%{smokesopranoclient_major}*

#-----------------------------------------------------------------------------

%define smokesopranoserver_major 3
%define libsmokesopranoserver %mklibname smokesopranoserver %{smokesopranoserver_major}

%package -n   %{libsmokesopranoserver}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokesopranoserver}
KDE generic bindings library.

%files -n %{libsmokesopranoserver}
%defattr(-,root,root)
%_kde_libdir/libsmokesopranoserver.so.%{smokesopranoserver_major}*

#-----------------------------------------------------------------------------

%define smokekdecore_major 3
%define libsmokekdecore %mklibname smokekdecore %{smokekdecore_major}

%package -n   %{libsmokekdecore}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokekdecore}
KDE generic bindings library.

%files -n %{libsmokekdecore}
%defattr(-,root,root)
%_kde_libdir/libsmokekdecore.so.%{smokekdecore_major}*

#-----------------------------------------------------------------------------

%define smokekdeui_major 3
%define libsmokekdeui %mklibname smokekdeui %{smokekdeui_major}

%package -n   %{libsmokekdeui}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokekdeui}
KDE generic bindings library.

%files -n %{libsmokekdeui}
%defattr(-,root,root)
%_kde_libdir/libsmokekdeui.so.%{smokekdeui_major}*

#-----------------------------------------------------------------------------

%define smokekfile_major 3
%define libsmokekfile %mklibname smokekfile %{smokekfile_major}

%package -n   %{libsmokekfile}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokekfile}
KDE generic bindings library.

%files -n %{libsmokekfile}
%defattr(-,root,root)
%_kde_libdir/libsmokekfile.so.%{smokekfile_major}*

#-----------------------------------------------------------------------------

%define smokekio_major 3
%define libsmokekio %mklibname smokekio %{smokekio_major}

%package -n   %{libsmokekio}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokekio}
KDE generic bindings library.

%files -n %{libsmokekio}
%defattr(-,root,root)
%_kde_libdir/libsmokekio.so.%{smokekio_major}*

#-----------------------------------------------------------------------------

%define smokeknewstuff2_major 3
%define libsmokeknewstuff2 %mklibname smokeknewstuff2_ %{smokeknewstuff2_major}

%package -n   %{libsmokeknewstuff2}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeknewstuff2}
KDE generic bindings library.

%files -n %{libsmokeknewstuff2}
%defattr(-,root,root)
%_kde_libdir/libsmokeknewstuff2.so.%{smokeknewstuff2_major}*

#-----------------------------------------------------------------------------

%define smokeknewstuff3_major 3
%define libsmokeknewstuff3 %mklibname smokeknewstuff3_ %{smokeknewstuff3_major}

%package -n   %{libsmokeknewstuff3}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeknewstuff3}
KDE generic bindings library.

%files -n %{libsmokeknewstuff3}
%defattr(-,root,root)
%_kde_libdir/libsmokeknewstuff3.so.%{smokeknewstuff3_major}*

#-----------------------------------------------------------------------------

%define smokekhtml_major 3
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

%define smokektexteditor_major 3
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

%define smokekparts_major 3
%define libsmokekparts %mklibname smokekparts %{smokekparts_major}

%package -n   %{libsmokekparts}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokekparts}
KDE generic bindings library.

%files -n %{libsmokekparts}
%defattr(-,root,root)
%_kde_libdir/libsmokekparts.so.%{smokekparts_major}*

#-----------------------------------------------------------------------------

%define smokekutils_major 3
%define libsmokekutils %mklibname smokekutils %{smokekutils_major}

%package -n   %{libsmokekutils}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokekutils}
KDE generic bindings library.

%files -n %{libsmokekutils}
%defattr(-,root,root)
%_kde_libdir/libsmokekutils.so.%{smokekutils_major}*

#-----------------------------------------------------------------------------

%define smokephonon_major 3
%define libsmokephonon %mklibname smokephonon %{smokephonon_major}

%package -n   %{libsmokephonon}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokephonon}
KDE generic bindings library.

%files -n %{libsmokephonon}
%defattr(-,root,root)
%_kde_libdir/libsmokephonon.so.%{smokephonon_major}*

#-----------------------------------------------------------------------------

%define smokeqtuitools_major 3
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

%define smokeqtwebkit_major 3
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

%define smokesolid_major 3
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

%define smokeokular_major 3
%define libsmokeokular %mklibname smokeokular %{smokeokular_major}

%package -n   %{libsmokeokular}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeokular}
KDE generic bindings library.

%files -n %{libsmokeokular}
%defattr(-,root,root)
%_kde_libdir/libsmokeokular.so.%{smokeokular_major}*

#-----------------------------------------------------------------------------

%define smokeqimageblitz_major 3
%define libsmokeqimageblitz %mklibname smokeqimageblitz %{smokeqimageblitz_major}

%package -n   %{libsmokeqimageblitz}
Summary:      KDE generic bindings library
Group:        Development/KDE and Qt

%description -n %{libsmokeqimageblitz}
KDE generic bindings library.

%files -n %{libsmokeqimageblitz}
%defattr(-,root,root)
%_kde_libdir/libsmokeqimageblitz.so.%{smokeqimageblitz_major}*

#-----------------------------------------------------------------------------

%define smokeqsci_major 3
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

%define lib_smokesoprano_major 3
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

%define lib_smokeqtscript_major 3
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

%define lib_smoke_qt_major 3
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

%define libsmokeplasma_major 3
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

%define libsmokenepomuk_major 3
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

%define libsmokeqttest_major 3
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

%define libsmokeakonadi_major 3
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

%define libsmokeattica_major 3
%define libsmokeattica %mklibname smokeattica %{libsmokeattica_major}

%package -n %{libsmokeattica}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{libsmokeattica}
Qt generic bindings library.

%files -n %{libsmokeattica}
%defattr(-,root,root)
%_kde_libdir/libsmokeattica.so.%{libsmokeattica_major}*

#------------------------------------------------------------

%define libsmokenepomukquery_major 3
%define libsmokenepomukquery %mklibname smokenepomukquery %{libsmokenepomukquery_major}

%package -n %{libsmokenepomukquery}
Summary: Qt generic bindings library
Group: Development/KDE and Qt

%description -n %{libsmokenepomukquery}
Qt generic bindings library.

%files -n %{libsmokenepomukquery}
%defattr(-,root,root)
%_kde_libdir/libsmokenepomukquery.so.%{libsmokenepomukquery_major}*

#------------------------------------------------------------

%package -n smoke4-devel
Summary: Header files for libsmoke
Group: Development/KDE and Qt
Requires: %{libsmokeplasma} = %epoch:%version-%release
Requires: %{lib_smoke_qt} = %epoch:%version-%release
Requires: %{libsmokeqsci} = %epoch:%version-%release
Requires: %{lib_smokeqtscript} = %epoch:%version-%release
Requires: %{libsmokeokular} = %epoch:%version-%release
Requires: %{libsmokesolid} = %epoch:%version-%release
Requires: %{libsmokeqtwebkit} = %epoch:%version-%release
Requires: %{libsmokeqtuitools} = %epoch:%version-%release
Requires: %{libsmokektexteditor} = %epoch:%version-%release
Requires: %{libsmokekhtml} = %epoch:%version-%release
Requires: %{libsmokeakonadi} = %epoch:%version-%release
Requires: %{libsmokenepomuk} = %epoch:%version-%release
Requires: %{libsmokeqttest} = %epoch:%version-%release
Requires: %{libsmokeqimageblitz} = %epoch:%version-%release
Requires: %{libsmokekdecore} = %epoch:%version-%release
Requires: %{libsmokekdeui} = %epoch:%version-%release
Requires: %{libsmokekfile} = %epoch:%version-%release
Requires: %{libsmokekio} = %epoch:%version-%release
Requires: %{libsmokeknewstuff2} = %epoch:%version-%release
Requires: %{libsmokeknewstuff3} = %epoch:%version-%release
Requires: %{libsmokekparts} = %epoch:%version-%release
Requires: %{libsmokekutils} = %epoch:%version-%release
Requires: %{libsmokephonon} = %epoch:%version-%release
Requires: %{libsmokeqtgui} = %epoch:%version-%release
Requires: %{libsmokeqtmultimedia} = %epoch:%version-%release
Requires: %{libsmokeqtnetwork} = %epoch:%version-%release
Requires: %{libsmokeqtopengl} = %epoch:%version-%release
Requires: %{libsmokeqtsql} = %epoch:%version-%release
Requires: %{libsmokeqtsvg} = %epoch:%version-%release
Requires: %{libsmokeqtxml} = %epoch:%version-%release
Requires: %{libsmokeqtxmlpatterns} = %epoch:%version-%release
Requires: %{libsmokesopranoclient} = %epoch:%version-%release
Requires: %{libsmokesopranoserver} = %epoch:%version-%release
Requires: %{libsmokeattica} = %epoch:%version-%release
Requires: %{libsmokenepomukquery} = %epoch:%version-%release
Provides: libsmoke2-devel = %epoch:%version-%release
Obsoletes: smoke-devel <= 1:3.5.10-3

%description -n smoke4-devel
Smoke devel files.

%files -n smoke4-devel
%defattr(-,root,root)
%_kde_bindir/smokeapi
%_kde_bindir/smokegen
%_kde_includedir/smoke.h
%_kde_includedir/smoke
%_kde_libdir/libsmoke*.so
%_kde_libdir/libcppparser.so
%_kde_libdir/smokegen

#------------------------------------------------------------

%ifnarch %arm %mips
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
%_prefix/lib/mono/qyoto/qt-dotnet.dll
%_prefix/lib/mono/qyoto/qscintilla.dll
%_prefix/lib/mono/qyoto/qtscript.dll
%_prefix/lib/mono/qyoto/qtuitools.dll
%_prefix/lib/mono/qyoto/qtwebkit.dll
%_prefix/lib/mono/qyoto/qttest.dll
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
%endif

#------------------------------------------------------------

%package -n php-qt4
Summary: PHP KDE 4 bindings
Group: Development/KDE and Qt
Requires: php-cli
Obsoletes: phpqt

%description -n php-qt4
PHP KDE 4 bindings

%files -n php-qt4
%defattr(-,root,root)
%_kde_bindir/phpuic
%_kde_libdir/php/extensions/php_qt.so

#------------------------------------------------------------

%if %with falcon

%package -n falcon-kde4
Summary: Falcon KDE 4 bindings
Group: Development/KDE and Qt
Requires: falcon

%description -n falcon-kde4
Falcon KDE 4 bindings

%files -n falcon-kde4
%defattr(-,root,root)
%_kde_libdir/kde4/krossfalcon.so

%endif

#------------------------------------------------------------
%ifnarch %arm %mips
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
%_prefix/lib/mono/qyoto/kde-dotnet.dll
%_prefix/lib/mono/qyoto/khtml-dll.dll
%_prefix/lib/mono/qyoto/soprano.dll
%_prefix/lib/mono/qyoto/akonadi.dll
%_prefix/lib/mono/qyoto/ktexteditor-dotnet.dll
%_prefix/lib/mono/qyoto/plasma-dll.dll
%_prefix/lib/mono/qyoto/nepomuk-dll.dll
%_prefix/lib/mono/qyoto/qimageblitz.dll
%_prefix/lib/mono/gac/kde-dotnet
%_prefix/lib/mono/gac/khtml-dll
%_prefix/lib/mono/gac/soprano
%_prefix/lib/mono/gac/akonadi
%_prefix/lib/mono/gac/ktexteditor-dotnet
%_prefix/lib/mono/gac/plasma-dll
%_prefix/lib/mono/gac/nepomuk-dll
%_prefix/lib/mono/gac/qimageblitz
%{_kde_libdir}/kde4/kimonopluginfactory.so
%_kde_libdir/libkhtml-sharp.so
%_kde_libdir/libnepomuk-sharp.so
%_kde_libdir/libsoprano-sharp.so
%_kde_libdir/libkimono.so
%_kde_libdir/libakonadi-sharp.so
%_kde_libdir/libktexteditor-sharp.so
%_kde_libdir/libplasma-sharp.so
%_kde_libdir/libqimageblitz-sharp.so
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
%_kde_libdir/pkgconfig/qyoto.pc
%_kde_libdir/pkgconfig/qtscript-sharp.pc
%_kde_libdir/pkgconfig/qttest-sharp.pc
%_kde_libdir/pkgconfig/qtuitools-sharp.pc
%_kde_libdir/pkgconfig/qtwebkit-sharp.pc

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
%endif

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
Obsoletes: ruby-qt < 1:3.5.10-3

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
%ruby_sitearchdir/okular.so
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
%ruby_sitelibdir/okular

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
%ruby_sitearchdir/nepomuk.so
%ruby_sitelibdir/KDE
%ruby_sitelibdir/khtml
%ruby_sitelibdir/ktexteditor
%ruby_sitelibdir/soprano
%ruby_sitelibdir/nepomuk
%ruby_sitelibdir/solid

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
%if %branch
%setup -q -n kdebindings-%version%kde_snapshot
%else
%setup -q -n kdebindings-%version
%endif

%build
# Remove invalid install dir
rm -f csharp/plasma/examples/CMakeLists.txt

export JAVA_HOME=%{java_home}

%cmake_kde4 \
	%if %with java
	-DENABLE_KROSSJAVA=TRUE \
	%else
	-DENABLE_KROSSJAVA=FALSE \
	%endif
    %if 1
	-DENABLE_PHP-QT=TRUE \
    %else
    -DENABLE_PHP-QT=FALSE \
    %endif
	-DENABLE_QSCINTILLA_SHARP=ON \
	-DENABLE_QSCINTILLA_RUBY=ON \
	-DENABLE_SMOKEKDEVPLATFORM=ON \
    -DENABLE_SMOKE=ON \
	%if %with falcon
	-DENABLE_KROSSFALCON=ON
	%endif

LD_LIBRARY_PATH=`pwd`/generator/bin %make

%install
rm -fr %buildroot
%makeinstall_std -C build

# Copy Python Doc
%{__mkdir_p} %{buildroot}%_datadir/doc/python-kde4
%{__cp} -a python/pykde4/docs/html/*  %{buildroot}%_datadir/doc/python-kde4/

%clean
rm -fr %buildroot

