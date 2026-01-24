%global toolchain clang
%undefine _cmake_shared_libs

Name:           pcsx2-stable
Version:        2.6.2
Release:        %autorelease
Summary:        PlayStation 2 Emulator
License:        GPLv3+
URL:            https://github.com/PCSX2/pcsx2

Source0:        %{url}/archive/v%{version}/pcsx2-%{version}.tar.gz

Patch0:         warn-unofficial-build.patch
Patch1:         allow-version-override.patch
Patch2:         adjust-required-versions.patch

Provides:       pcsx2
Conflicts:      pcsx2

BuildRequires:  clang llvm cmake extra-cmake-modules
BuildRequires:  cmake(KDDockWidgets-qt6) >= 2.0.0
BuildRequires:  cmake(plutovg)           >= 1.1.0
BuildRequires:  cmake(plutosvg)          >= 0.0.7
BuildRequires:  cmake(Qt6Core)           >= 6.7.3
BuildRequires:  cmake(Qt6CoreTools)      >= 6.7.3
BuildRequires:  cmake(Qt6Gui)            >= 6.7.3
BuildRequires:  cmake(Qt6GuiTools)       >= 6.7.3
BuildRequires:  cmake(Qt6Widgets)        >= 6.7.3
BuildRequires:  cmake(Qt6WidgetsTools)   >= 6.7.3
BuildRequires:  cmake(Qt6LinguistTools)  >= 6.7.3
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(SDL3)              >= 3.2.6
BuildRequires:  cmake(WebP)              >= 1.3.2
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(freetype2)     >= 2.11.1
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libpng)        >= 1.6.40
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt6-qtbase-private-devel
Requires:       pcsx2-patches
Requires:       qt6-qtsvg
Recommends:     libEGL
Recommends:     qt6-qtimageformats
Recommends:     qt6-qtwayland
Recommends:     vulkan

%description
PCSX2 is a free and open-source PlayStation 2 (PS2) emulator. Its purpose is to emulate the PS2's hardware, using a combination of MIPS CPU Interpreters, Recompilers and a Virtual Machine which manages hardware states and PS2 system memory. This allows you to play PS2 games on your PC, with many additional features and benefits.

%prep
%autosetup -p1 -n pcsx2-%{version}

%build
%cmake \
	-DPCSX2_GIT_REV_OVERRIDE=%{version}%{dist} \
	-DCMAKE_BUILD_TYPE=Release \
	-DUSE_LINKED_FFMPEG=ON \
	-DPACKAGE_MODE=ON \
	-DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON \
	-DUSE_BACKTRACE=OFF \
	-DDISABLE_ADVANCE_SIMD=ON

%cmake_build

%install
%cmake_install
rm -r %{buildroot}%{_datadir}/PCSX2/resources/shaders/dx11
install -Dm644 .github/workflows/scripts/linux/pcsx2-qt.desktop %{buildroot}%{_datadir}/applications/PCSX2.desktop
install -Dm644 bin/resources/icons/AppIconLarge.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/PCSX2.png

%files
%license COPYING.GPLv3 bin/docs/ThirdPartyLicenses.html
%doc bin/docs/GameIndex.pdf
%{_bindir}/pcsx2-qt
%{_datadir}/PCSX2/resources
%{_datadir}/PCSX2/translations
%{_datadir}/applications/PCSX2.desktop
%{_datadir}/icons/hicolor/256x256/apps/PCSX2.png

%post
setcap 'CAP_NET_RAW+eip CAP_NET_ADMIN+eip' %{_bindir}/pcsx2-qt

%changelog
%autochangelog
