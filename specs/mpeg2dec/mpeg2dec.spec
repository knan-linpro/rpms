# $Id$
# Authority: matthias

#define date 20030701

Summary: MPEG-2 and MPEG-1 decoding library and test program
Name: mpeg2dec
Version: 0.4.0
Release: %{?date:0.%{date}.}2b
License: LGPL
Group: System Environment/Libraries
URL: http://libmpeg2.sourceforge.net/
Source: http://libmpeg2.sourceforge.net/files/%{name}-%{?date:date}%{!?date:%{version}b}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: XFree86, /sbin/ldconfig
BuildRequires: XFree86-devel, pkgconfig, gcc-c++

%description
A free library for decoding MPEG-2 and MPEG-1 video streams.


%package devel
Summary: Development files for mpeg2dec's libmpeg2
Group: Development/Libraries
Requires: %{name} = %{version}, pkgconfig

%description devel
A free library for decoding MPEG-2 and MPEG-1 video streams.

This package contains files needed to build applications that use mpeg2dec's
libmpeg2.


%prep
%setup -n %{name}-%{version}%{?date:-cvs}

%build
%configure --enable-shared --disable-sdl
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/*
%{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Thu Feb  5 2004 Matthias Saou <http://freshrpms.net/> 0.4.0-2b.fr
- Update to 0.4.0b.

* Mon Jan  5 2004 Matthias Saou <http://freshrpms.net/> 0.4.0-1.fr
- Update to 0.4.0.

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 0.3.2-0.20030701.2.fr
- Rebuild for Fedora Core 1.

* Tue Jul  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to today's snapshot, enabled the spec to build snapshots since
  videolan-client 0.6.0 requires 0.3.2 cvs.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Thu Jan 16 2003 Matthias Saou <http://freshrpms.net/>
- Update to 0.3.1.

* Mon Oct 28 2002 Matthias Saou <http://freshrpms.net/>
- Major spec file cleanup.

* Mon Jun 17 2002 Thomas Vander Stichele <thomas@apestaart.org>
- remove .la
- release 3

* Wed May 29 2002 Thomas Vander Stichele <thomas@apestaart.org>
- wrote out the different libs
- added docs
- removed autogen.sh option

* Wed May 08 2002 Erik Walthinsen <omega@temple-baptist.com>
- changed whitespace
- removed %attr and changed %defattr to (-,root,root)

* Fri May 03 2002 Thomas Vander Stichele <thomas@apestaart.org>
- adapted from PLD spec for 0.2.1

