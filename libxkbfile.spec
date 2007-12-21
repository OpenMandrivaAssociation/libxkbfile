%define major 1
%define libname %mklibname xkbfile %{major}
%define develname %mklibname xkbfile -d
%define staticdevelname %mklibname xkbfile -d -s

Name: libxkbfile
Summary:  The xkbfile Library
Version: 1.0.4
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libxkbfile-%{version}.tar.bz2

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

BuildRoot: %{_tmppath}/%{name}-root

%description
The xkbfile Library.

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The xkbfile Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
The xkbfile Library.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} >= %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: %{name}-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %mklibname xkbfile 1 -d

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libxkbfile.so
%{_libdir}/libxkbfile.la
%{_libdir}/pkgconfig/xkbfile.pc
%{_includedir}/X11/extensions/XKM.h
%{_includedir}/X11/extensions/XKBrules.h
%{_includedir}/X11/extensions/XKBconfig.h
%{_includedir}/X11/extensions/XKMformat.h
%{_includedir}/X11/extensions/XKBfile.h
%{_includedir}/X11/extensions/XKBbells.h

#-----------------------------------------------------------

%package -n %{staticdevelname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} >= %{version}
Provides: %{name}-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %mklibname xkbfile 1 -d -s

%description -n %{staticdevelname}
Static development files for %{name}.

%files -n %{staticdevelname}
%defattr(-,root,root)
%{_libdir}/libxkbfile.a

#-----------------------------------------------------------

%prep
%setup -q -n libxkbfile-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libxkbfile.so.%{major}*
