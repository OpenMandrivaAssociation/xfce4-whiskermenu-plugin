%define debug_package %{nil}

Summary:	An alternate application launcher for Xfce
Name:		xfce4-whiskermenu-plugin
Version:	1.0.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
Url:		http://gottcode.org/xfce4-whiskermenu-plugin/
Source0:	http://gottcode.org/xfce4-whiskermenu-plugin/%{name}-%{version}-src.tar.bz2

BuildRequires:	cmake
BuildRequires:	pkgconfig(exo-1)
BuildRequires:	pkgconfig(garcon-1)
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1)
BuildRequires:	pkgconfig(libxfce4util-1.0)

%description
Whisker Menu is an alternate application launcher for Xfce.

%prep
%setup -q

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
