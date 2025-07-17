%define _unpackaged_files_terminate_build 0

Name:           plutovg-devel-cmake
Version:        1.1.0
Release:        %autorelease
Summary:        Tiny 2D vector graphics library in C
License:        MIT AND FTL
URL:            https://github.com/sammycage/plutovg

Source0:        %{url}/archive/v%{version}/plutovg-%{version}.tar.gz

BuildRequires:  gcc cmake
Requires:       plutovg-devel%{?_isa}

%description
CMake package files for plutovg

%prep
%autosetup -n plutovg-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_libdir}/cmake/plutovg

%changelog
%autochangelog
