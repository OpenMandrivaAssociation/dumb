%define major 2
%define libdumb %mklibname dumb %{major}
%define libaldmb %mklibname aldmb %{major}
%define devname %mklibname -d dumb

Summary:	Dynamic Universal Music Bibliotheque
Name:		dumb
Version:	2.0.3
Release:	4
License:	BSD
Group:		Sound
Url:		http://dumb.sf.net/
# Post-0.9.3 versions are at https://github.com/kode54/dumb
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig(allegro)
BuildRequires:	pkgconfig(argtable2)
#BuildRequires:	cmake(SDL2)
BuildRequires:  pkgconfig(sdl2)

%description
DUMB is an IT, XM, S3M and MOD player library. This includes a player based
on Allegro.

%files
%doc README.md LICENSE
%{_bindir}/*

#----------------------------------------------------------------------------

%package -n %{libdumb}
Summary:	Dynamic Universal Music Bibliotheque library
Group:		System/Libraries

%description -n %{libdumb}
DUMB is an IT, XM, S3M and MOD player library.

%files -n %{libdumb}
%{_libdir}/libdumb.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{libaldmb}
Summary:	Dynamic Universal Music Bibliotheque library for Allegro
Group:		System/Libraries
Requires:	%{libdumb} = %{EVRD}

%description -n %{libaldmb}
DUMB is an IT, XM, S3M and MOD player library for use with the Allegro library

%files -n %{libaldmb}
%{_libdir}/libaldmb.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Dynamic Universal Music Bibliotheque
Group:		Development/C
%rename dumb-devel
Requires:	%{libdumb} = %{EVRD}
Requires:	%{libaldmb} = %{EVRD}

%description -n %{devname}
DUMB is an IT, XM, S3M and MOD player library. This contains static libraries
and C header files.

%files -n %{devname}
%{_libdir}/lib*.so
%{_includedir}/*.h
%{_libdir}/pkgconfig/dumb.pc

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%cmake \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_STATIC_LIBS:BOOL=ON \
	-GNinja

%build
%ninja -C build

%install
%ninja_install -C build
