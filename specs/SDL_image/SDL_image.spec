# $Id$
# Authority: dries
# Upstream: Sam Latinga <slouken$devolution,com>

Summary: Load images as SDL surfaces
Name: SDL_image
Version: 1.2.4
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://www.libsdl.org/projects/SDL_image/
Source: http://www.libsdl.org/projects/SDL_image/release/SDL_image-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: SDL-devel, gcc-c++, automake, autoconf, perl, libjpeg-devel
BuildRequires: libpng-devel, zlib-devel

%description
SDL_image is an image file loading library. It loads images as SDL surfaces, 
and supports the following formats: BMP, PNM, XPM, LBM, PCX, GIF, JPEG, PNG, 
TGA.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%files
%defattr(-, root, root, 0755)
%doc CHANGES COPYING README
%{_libdir}/libSDL_image*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_libdir}/libSDL_image.a
%{_libdir}/libSDL_image.so
%{_includedir}/SDL/SDL_image.h
%exclude %{_libdir}/*.la

%changelog
* Sun Dec 04 2005 Dries Verachtert <dries@ulyssis.org - 1.2.4-1
- Initial package
