%define _unpackaged_files_terminate_build 0

Name:           plutosvg-devel-cmake
Version:        0.0.7
Release:        %autorelease
Summary:        Tiny SVG rendering library in C
License:        MIT
URL:            https://github.com/sammycage/plutosvg

Source0:        %{url}/archive/v%{version}/plutosvg-%{version}.tar.gz

BuildRequires:  gcc cmake
BuildRequires:  freetype-devel >= 2.12
BuildRequires:  cmake(plutovg) >= 1.0.0
Requires:       plutosvg-devel%{?_isa}

%description
CMake package files for plutosvg

%prep
%autosetup -n plutosvg-%{version}

%build
%cmake -DPLUTOSVG_ENABLE_FREETYPE=ON
%cmake_build

%install
%cmake_install

%files
%{_libdir}/cmake/plutosvg

%changelog
%autochangelog
