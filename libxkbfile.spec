%define major 1
%define libname %mklibname xkbfile %{major}
%define develname %mklibname xkbfile -d

Name: libxkbfile
Summary:  The xkbfile Library
Version: 1.0.8
Release: 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libxkbfile-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xkbfile Library.

%package -n %{libname}
Summary:  The xkbfile Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The xkbfile Library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} >= %{version}
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{_lib}xkbfile1-devel
Obsoletes: %{_lib}xkbfile-static-devel

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libxkbfile-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libname}
%{_libdir}/libxkbfile.so.%{major}*

%files -n %{develname}
%{_libdir}/libxkbfile.so
%{_libdir}/pkgconfig/xkbfile.pc
%{_includedir}/X11/extensions/XKM.h
%{_includedir}/X11/extensions/XKBrules.h
%{_includedir}/X11/extensions/XKBconfig.h
%{_includedir}/X11/extensions/XKMformat.h
%{_includedir}/X11/extensions/XKBfile.h
%{_includedir}/X11/extensions/XKBbells.h

