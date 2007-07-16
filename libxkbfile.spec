%define libxkbfile %mklibname xkbfile 1
Name: libxkbfile
Summary:  The xkbfile Library
Version: 1.0.4
Release: %mkrel 1
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libxkbfile-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
The xkbfile Library

#-----------------------------------------------------------

%package -n %{libxkbfile}
Summary:  The xkbfile Library
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxkbfile}
The xkbfile Library

#-----------------------------------------------------------

%package -n %{libxkbfile}-devel
Summary: Development files for %{name}
Group: Development/X11

Requires: %{libxkbfile} >= %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxkbfile-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxkbfile}-devel
Development files for %{name}

%pre -n %{libxkbfile}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxkbfile}-devel
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

%package -n %{libxkbfile}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxkbfile}-devel >= %{version}
Provides: libxkbfile-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxkbfile}-static-devel
Static development files for %{name}

%files -n %{libxkbfile}-static-devel
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxkbfile}
%defattr(-,root,root)
%{_libdir}/libxkbfile.so.1
%{_libdir}/libxkbfile.so.1.0.*


