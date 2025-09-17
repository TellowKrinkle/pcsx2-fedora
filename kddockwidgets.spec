%global sover 2.2

Name:           kddockwidgets2
Version:        2.2.5
Release:        2%{?dist}
Summary:        Qt dock widget library

License:        GPL-3.0-only AND GPL-2.0-only AND BSD-3-Clause
URL:            https://github.com/KDAB/KDDockWidgets
Source0:        %{url}/archive/v%{version}/kddockwidgets-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  doxygen
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  libxkbcommon-devel

%description
Qt dock widget library written by KDAB, suitable for replacing QDockWidget
and implementing advanced functionalities missing in Qt.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        qt6
Summary:        Qt dock widget library for Qt 6

%description    qt6
%{description}

%package        qt6-devel
Summary:        Development files for %{name}-qt6

Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}
%description    qt6-devel
The %{name}-qt6-devel package contains libraries and header files for
developing applications that use %{name}-qt6.


%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.


%prep
%autosetup -n KDDockWidgets-%{version}


%build
%global _vpath_builddir %{_target_platform}-qt5
%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%global _vpath_builddir %{_target_platform}-qt6
# qhelpgenerator needs to be in $PATH to be detected
export PATH=%{_qt6_libexecdir}:$PATH
%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DKDDockWidgets_FRONTENDS=qtwidgets \
    -DKDDockWidgets_QT6=ON \
    -DKDDockWidgets_DOCS=ON
%cmake_build

%install
%global _vpath_builddir %{_target_platform}-qt5
%cmake_install
rm -r %{buildroot}%{_datadir}/doc

%global _vpath_builddir %{_target_platform}-qt6
%cmake_install
mkdir -p %{buildroot}%{_qt6_docdir}
mv %{buildroot}%{_docdir}/KDDockWidgets-qt6/*.qch %{buildroot}%{_qt6_docdir}/
mv %{buildroot}%{_docdir}/KDDockWidgets-qt6/*.tags %{buildroot}%{_qt6_docdir}/
rm -r %{buildroot}%{_datadir}/doc/KDDockWidgets-qt6

%files
%license LICENSES/* LICENSE.txt
%doc CONTRIBUTORS.txt Changelog README.md
%{_libdir}/libkddockwidgets.so.%{sover}*

%files devel
%{_includedir}/kddockwidgets
%{_libdir}/cmake/KDDockWidgets
%{_libdir}/libkddockwidgets.so
%{_libdir}/qt5/mkspecs/modules/qt_KDDockWidgets.pri

%files qt6
%license LICENSES/* LICENSE.txt
%doc CONTRIBUTORS.txt Changelog README.md
%{_libdir}/libkddockwidgets-qt6.so.%{sover}*

%files qt6-devel
%{_includedir}/kddockwidgets-qt6
%{_libdir}/cmake/KDDockWidgets-qt6
%{_libdir}/libkddockwidgets-qt6.so
%{_libdir}/qt6/mkspecs/modules/qt_KDDockWidgets.pri
%{_qt6_docdir}/kddockwidgets.tags

%files doc
%{_qt6_docdir}/kddockwidgets-api.qch

%changelog
* Wed Jul 16 2025 TellowKrinkle <tellowkrinkle@gmail.com> - 2.2.5-1
- Update to 2.2.5

* Tue Mar 12 2024 Marie Loise Nolden <loise@kde.org> - 2.0.0-1
- update to 2.0.0
- add qch docs for Qt Creator/KDevelop

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-6
- Rebuild (qt6)

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Jan Grulich <jgrulich@redhat.com> - 1.7.0-3
- Rebuild (qt5)

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 1.7.0-2
- Rebuild (qt6)

* Tue Oct 31 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.7.0-1
- Update to 1.7.0

* Fri Oct 13 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-13
- Rebuild (qt6)

* Mon Oct 09 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-12
- Rebuild (qt5)

* Thu Oct 05 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-11
- Rebuild (qt6)

* Mon Jul 24 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-10
- Rebuild (qt6)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-8
- Rebuild for qtbase private API version change

* Wed Jul 12 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-7
- Rebuild for qtbase private API version change

* Wed Jun 14 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-6
- Rebuild (qt5)

* Fri May 26 2023 Jan Grulich <jgrulich@redhat.com> - 1.6.0-5
- Rebuild (qt6)

* Fri Apr 14 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.6.0-3
- Rebuild for new Qt 5 version

* Tue Apr 11 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.6.0-3
- Add Qt6 version

* Tue Mar 28 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.6.0-2
- Pin Qt5 version

* Fri Mar 24 2023 Vasiliy Glazov <vascom2@gmail.com> - 1.6.0-1
- Initial packaging.
