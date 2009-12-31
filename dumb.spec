%define name dumb
%define version 0.9.3
%define release %mkrel 7

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


