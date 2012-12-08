%define major 1
%define libname %mklibname xkbfile %{major}
%define develname %mklibname xkbfile -d

Name:		libxkbfile
Summary:	The xkbfile Library
Version:	1.0.8
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libxkbfile-%{version}.tar.bz2

BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
The xkbfile Library.

%package -n %{libname}
Summary:	The xkbfile Library
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libname}
The xkbfile Library.

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	libxorg-x11-devel < 7.0
Obsoletes:	%{_lib}xkbfile1-devel < 1.0.8
Obsoletes:	%{_lib}xkbfile-static-devel < 1.0.8

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


%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.0.8-1
+ Revision: 783807
- version update 1.0.8

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0.7-4
+ Revision: 783367
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.0.7-3
+ Revision: 745743
- rebuild
- disabled static build
- removed .la files
- cleaned up spec

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.7-2
+ Revision: 660301
- mass rebuild

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.0.7-1mdv2011.0
+ Revision: 590569
- new release

* Mon Nov 09 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.6-1mdv2010.1
+ Revision: 463735
- New version: 1.0.6

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.5-3mdv2010.0
+ Revision: 425928
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-2mdv2009.0
+ Revision: 264977
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Apr 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0.5-1mdv2009.0
+ Revision: 192985
- new release

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Tue Jan 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.4-4mdv2008.1
+ Revision: 152804
- Update BuildRequires and rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-3mdv2008.1
+ Revision: 150860
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Jul 21 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.4-2mdv2008.0
+ Revision: 54099
- fix typo preventing static-devel package from correctly obsoleting the previous version

* Mon Jul 16 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.0.4-1mdv2008.0
+ Revision: 52771
- new devel library policy
- spec file clean
- new version

