# $Id$
# Authority: matthias

Summary: A rewrite of the xawtv webcam app, which adds imlib2 support.
Name: camE
Version: 1.7
Release: 2
License: GPL
Group: System Environment/Daemons
Source: http://linuxbrit.co.uk/downloads/camE-%{version}.tar.gz
URL: http://linuxbrit.co.uk/camE/
BuildRoot: %{_tmppath}/%{name}-root
Requires: giblib >= 1.2.3, imlib2, curl, zlib
BuildRequires: XFree86-devel, giblib-devel >= 1.2.3, imlib2-devel, curl-devel
BuildRequires: zlib-devel

%description
camE is a rewrite of the xawtv webcam app, which adds imlib2 support and
thus many new possibilities.

%prep
%setup

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING *.style example.camErc*
%{_bindir}/%{name}

%changelog
* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> 1.7-2.fr
- Rebuild for Fedora Core 1.
- Added missing zlib dependency.

* Wed Oct  1 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.7.

* Mon Jun 23 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.6.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.

* Wed Mar 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.5.

* Wed Feb 26 2003 Matthias Saou <http://freshrpms.net/>
- Update to 1.4.

* Sun Jan 12 2003 Matthias Saou <http://freshrpms.net/>
- Added missing imlib2 dependency.

* Wed Nov 13 2002 Matthias Saou <http://freshrpms.net/>
- Rebuilt against Red Hat Linux 8.0.

* Fri May  3 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

