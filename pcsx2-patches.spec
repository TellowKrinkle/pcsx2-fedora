%global commit __COMMIT__
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global timestamp %(date +%%Y%%m%%d)

Name:           pcsx2-patches
Version:        0~git%{timestamp}.%{shortcommit}
Release:        %autorelease
Summary:        Widescreen and no interlace patches for PCSX2
License:        GPLv3+
URL:            https://github.com/PCSX2/pcsx2_patches

Source0:        %{url}/archive/%{commit}/pcsx2_patches-%{commit}.tar.gz

BuildRequires:  zip
BuildArch:      noarch

%description
Widescreen and no interlace patches for PCSX2

These are the patches used by the PCSX2 emulator to add widescreen support
or disable interlace as needed.

%prep
%autosetup -n pcsx2_patches-%{commit}

%build
zip -j9 patches.zip patches/*

%install
install -Dm644 patches.zip %{buildroot}%{_datadir}/PCSX2/resources/patches.zip

%files
%{_datadir}/PCSX2/resources/patches.zip

%changelog
%autochangelog
