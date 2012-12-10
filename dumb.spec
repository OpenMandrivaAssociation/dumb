%define name dumb
%define version 0.9.3
%define release %mkrel 9

Summary: Dynamic Universal Music Bibliotheque
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/dumb/%{name}-%{version}.tar.bz2
Patch: dumb-0.9.3-fix-linking.patch
License: BSD-like
Group: Sound
Url: http://dumb.sf.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: liballegro-devel

%description
DUMB is an IT, XM, S3M and MOD player library. This includes a player based
on Allegro.

%package devel
Group: Development/C
Summary: Dynamic Universal Music Bibliotheque
%description devel
DUMB is an IT, XM, S3M and MOD player library. This contains static libraries
and C header files.

%prep
%setup -q
%patch -p1

cat > make/config.txt << EOF
include make/unix.inc
ALL_TARGETS := core core-examples core-headers
ALL_TARGETS += allegro allegro-examples allegro-headers
PREFIX := %_prefix
EOF

%build
%make CC="gcc -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%_bindir,%_includedir,%_libdir}
%makeinstall PREFIX=%buildroot%_prefix LIB_INSTALL_PATH=%buildroot%_libdir
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc readme.txt licence.txt release.txt
%_bindir/*

%files devel
%defattr(-,root,root)
%doc docs/*
%_libdir/lib*.a
%_includedir/*.h




%changelog
* Tue Dec 06 2011 Götz Waschk <waschk@mandriva.org> 0.9.3-9mdv2012.0
+ Revision: 738171
- work around rpm5 breakage
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.3-8mdv2011.0
+ Revision: 610289
- rebuild

* Thu Dec 31 2009 Emmanuel Andry <eandry@mandriva.org> 0.9.3-7mdv2010.1
+ Revision: 484586
- rebuild for new allegro

* Fri Jul 24 2009 Götz Waschk <waschk@mandriva.org> 0.9.3-6mdv2010.0
+ Revision: 399217
- fix linking

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.9.3-5mdv2009.0
+ Revision: 244555
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Mon Dec 04 2006 Götz Waschk <waschk@mandriva.org> 0.9.3-3mdv2007.0
+ Revision: 90351
- Import dumb

* Mon Dec 04 2006 Götz Waschk <waschk@mandriva.org> 0.9.3-3mdv2007.1
- rebuild

* Fri Dec 02 2005 Götz Waschk <waschk@mandriva.org> 0.9.3-2mdk
- fix build on x86_64

* Fri Sep 30 2005 Götz Waschk <waschk@mandriva.org> 0.9.3-1mdk
- initial package

