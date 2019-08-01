%define debug_package %{nil}
%define url_ver %(echo %version | cut -d. -f1,2)

Summary:	An alternate application launcher for Xfce
Name:		xfce4-whiskermenu-plugin
Version:	2.3.2
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://gottcode.org/xfce4-whiskermenu-plugin/
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-whiskermenu-plugin/%{url_ver}/%{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	pkgconfig(exo-2)
BuildRequires:	pkgconfig(garcon-1)
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(pangoxft)

%description
Whisker Menu is an alternate application launcher for Xfce.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README NEWS
%{_bindir}/xfce4-popup-whiskermenu
%{_libdir}/xfce4/panel/plugins/libwhiskermenu.so
%{_datadir}/xfce4/panel/plugins/whiskermenu.desktop
%{_iconsdir}/*/*/apps/xfce4-whiskermenu.*g
%{_mandir}/man1/xfce4-popup-whiskermenu.1.*

