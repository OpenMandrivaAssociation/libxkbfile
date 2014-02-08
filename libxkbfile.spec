%define major 1
%define libname %mklibname xkbfile %{major}
%define devname %mklibname xkbfile -d

Summary:	The xkbfile Library
Name:		libxkbfile
Version:	1.0.8
Release:	6
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libxkbfile-%{version}.tar.bz2
Patch0:		libxkb-aarch64.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
The xkbfile Library.

%package -n %{libname}
Summary:	The xkbfile Library
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
The xkbfile Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%setup -qn libxkbfile-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libxkbfile.so.%{major}*

%files -n %{devname}
%{_libdir}/libxkbfile.so
%{_libdir}/pkgconfig/xkbfile.pc
%{_includedir}/X11/extensions/XKM.h
%{_includedir}/X11/extensions/XKBrules.h
%{_includedir}/X11/extensions/XKBconfig.h
%{_includedir}/X11/extensions/XKMformat.h
%{_includedir}/X11/extensions/XKBfile.h
%{_includedir}/X11/extensions/XKBbells.h

