Summary:	Dynamic Universal Music Bibliotheque
Name:		dumb
Version:	0.9.3
Release:	10
License:	BSD
Group:		Sound
Url:		http://dumb.sf.net/
Source0:	http://prdownloads.sourceforge.net/dumb/%{name}-%{version}.tar.bz2
Patch0:		dumb-0.9.3-fix-linking.patch
BuildRequires:	pkgconfig(allegro)

%description
DUMB is an IT, XM, S3M and MOD player library. This includes a player based
on Allegro.

%files
%doc readme.txt licence.txt release.txt
%{_bindir}/*

#----------------------------------------------------------------------------

%package devel
Summary:	Dynamic Universal Music Bibliotheque
Group:		Development/C

%description devel
DUMB is an IT, XM, S3M and MOD player library. This contains static libraries
and C header files.

%files devel
%doc docs/*
%{_libdir}/lib*.a
%{_includedir}/*.h

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

cat > make/config.txt << EOF
include make/unix.inc
ALL_TARGETS := core core-examples core-headers
ALL_TARGETS += allegro allegro-examples allegro-headers
PREFIX := %{_prefix}
EOF

%build
%make CC="gcc -fPIC %{optflags}" LDFLAGS="%{ldflags}"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}
%makeinstall \
	PREFIX=%{buildroot}%{_prefix} \
	LIB_INSTALL_PATH=%{buildroot}%{_libdir}

