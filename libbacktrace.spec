%global commit ad106d5fdd5d960bd33fae1c48a351af567fd075
%global cdate 2023.01.06
%global debug_package %{nil}

Name:           libbacktrace
Version:        %{cdate}
Release:        %autorelease
Summary:        A C library that may be linked into a C/C++ program to produce symbolic backtraces
License:        BSD-3-Clause
URL:            https://github.com/ianlancetaylor/libbacktrace

Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  gcc

%description
A C library that may be linked into a C/C++ program to produce symbolic backtraces

%prep
%autosetup -n %{name}-%{commit}

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_includedir}/backtrace-supported.h
%{_includedir}/backtrace.h
%{_libdir}/libbacktrace.a

%changelog
%autochangelog
