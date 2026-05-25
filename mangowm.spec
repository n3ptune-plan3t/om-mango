Name:           mangowm
Version:        0.13.1
Release:        1
Summary:        A modern, lightweight, high-performance Wayland compositor built on dwl
License:        GPL-3.0-or-later AND MIT AND X11 AND CC0-1.0
Group:          Graphical desktop/Other
URL:            https://github.com/mangowm/mangowc
Source0:        https://github.com/mangowm/mango/archive/refs/tags/%{version}/%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(scenefx-0.4)

%description
MangoWM is a modern, lightweight, high-performance Wayland compositor built on
dwl — crafted for speed, flexibility, and a customizable desktop experience.

%prep
%autosetup -n mango-%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%license LICENSE.wlroots
%license LICENSE.tinywl
%license LICENSE.sway
%license LICENSE.dwm
%license LICENSE.dwl
%{_bindir}/mango
%{_bindir}/mmsg
%config %{_sysconfdir}/mango/config.conf
%{_datadir}/wayland-sessions/mango.desktop
%{_datadir}/xdg-desktop-portal/mango-portals.conf
