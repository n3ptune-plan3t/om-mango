%define pkgname mangowm
%define _pkgname mango

Name:           %{pkgname}
Version:        0.13.1
Release:        1
Summary:        A Wayland compositor with smooth animation
License:        GPLv3
Group:          Graphical desktop/Other
URL:            https://github.com/DreamMaoMao/mangowc
Source0:        https://github.com/mangowm/mango/archive/refs/tags/%{version}/%{_pkgname}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(wayland-client) >= 1.23.1
BuildRequires:  pkgconfig(wayland-protocols) >= 1.41
BuildRequires:  pkgconfig(libinput) >= 1.27.1
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(libxkbcommon)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(scenefx-0.4)

Requires:       glibc
Provides:       wayland-compositor
Provides:       mangowc = %{version}-%{release}
Obsoletes:      mangowc < %{version}-%{release}

%description
A Wayland compositor with smooth animation.

%prep
%autosetup -n %{_pkgname}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE*
%doc README*
%{_bindir}/*
