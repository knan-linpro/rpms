# $Id$
# Authority: matthias

%define desktop_vendor freshrpms

Summary: The Open Racing Car Simulator
Name: torcs
Version: 1.2.2
Release: 1
License: GPL
Group: Amusements/Games
URL: http://torcs.org/
Source: http://dl.sf.net/torcs/TORCS-%{version}-src.tgz
Source1: http://dl.sf.net/torcs/TORCS-%{version}-src-robots-base.tgz
Source2: http://dl.sf.net/torcs/TORCS-%{version}-src-robots-berniw.tgz
Source3: http://dl.sf.net/torcs/TORCS-%{version}-src-robots-K1999.tgz
Source4: http://dl.sf.net/torcs/TORCS-%{version}-src-robots-billy.tgz
Source5: http://dl.sf.net/torcs/TORCS-%{version}-src-robots-bt.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: torcs-data, glut, plib >= 1.6.0
BuildRequires: XFree86-devel, XFree86-Mesa-libGLU, XFree86-Mesa-libGL
BuildRequires: gcc-c++, plib >= 1.6.0, glut-devel
BuildRequires: libpng-devel, libjpeg-devel, zlib-devel
BuildRequires: desktop-file-utils

%description
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse. 


%package robots
Summary: The Open Racing Car Simulator robots
Group: Amusements/Games
Requires: %{name}

%description robots
TORCS is a 3D racing cars simulator using OpenGL.  The goal is to have
programmed robots drivers racing against each others.  You can also drive
yourself with either a wheel, keyboard or mouse.

This package contains the robots who can race on their own.


%prep
%setup -a 1 -a 2 -a 3 -a 4 -a 5
# Put the drivers back where they belong
mv %{name}-%{version}/src/drivers/* src/drivers/


%build
%configure
%{__make} %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%{__install} -m 644 -D Ticon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

cat > %{name}.desktop << EOF
[Desktop Entry]
Name=TORCS
Comment=%{summary}
Exec=%{name}
Icon=%{name}.png
Terminal=false
Type=Application
EOF

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor %{desktop_vendor} \
  --dir %{buildroot}%{_datadir}/applications    \
  --add-category X-Red-Hat-Extra                \
  --add-category Application                    \
  --add-category Game                           \
  %{name}.desktop


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-, root, root, 0755)
%doc CHANGELOG.html COPYING README.linux TODO.html
%{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/drivers
%{_libdir}/%{name}/drivers/human
%{_libdir}/%{name}/lib
%{_libdir}/%{name}/modules
%{_libdir}/%{name}/setup_linux.sh
%{_libdir}/%{name}/*-bin
%{_datadir}/applications/%{desktop_vendor}-%{name}.desktop
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/config
%dir %{_datadir}/games/%{name}/drivers
%{_datadir}/games/%{name}/drivers/human
%{_datadir}/games/%{name}/results
%{_datadir}/games/%{name}/telemetry
%{_datadir}/pixmaps/%{name}.png


%files robots
%defattr(-, root, root, 0755)
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/drivers
# Easier this way, since we package them all-minus-one in ;-)
%exclude %{_libdir}/%{name}/drivers/human
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/drivers
%exclude %{_datadir}/games/%{name}/drivers/human


%changelog
* Thu Feb 26 2004 Matthias Saou <http://freshrpms.net/> 1.2.2-1.fr
- Update to 1.2.2.
- No longer require compat-libstdc++-devel for building.
- This version broke %%makeinstall, so switch to DESTDIR method.
- Re-enabled K1999 build, it works again.
- Added new robots : billy and bt.

* Tue Jan 13 2004 Matthias Saou <http://freshrpms.net/> 1.2.1-4.fr
- Work around the XFree86 dependency problem by adding XFree86-Mesa-libGLU.

* Tue Dec  2 2003 Matthias Saou <http://freshrpms.net/> 1.2.1-3.fr
- Rebuild for Fedora Core 1.
- Disabled build of the K1999 driver (strstream.h seems obsolete).

* Tue May 27 2003 Matthias Saou <http://freshrpms.net/>
- Added a torcs requirement to the robots package.

* Wed Apr 23 2003 Matthias Saou <http://freshrpms.net/>
- Initial RPM release.

