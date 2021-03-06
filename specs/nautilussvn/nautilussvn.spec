# $Id$
# Authority: shuff

## DistExclude: el3 el4

%define python_sitearch %(%{__python} -c 'from distutils import sysconfig; print sysconfig.get_python_lib(1)')
%define nautilus_extensiondir %(pkg-config --variable=extensiondir libnautilus-extension)

Summary: Nautilus integration for Subversion
Name: nautilussvn
Version: 0.12
Release: 1%{?dist}
License: GPL
Group: Development/Libraries
URL: http://code.google.com/p/nautilussvn/

Source: http://nautilussvn.googlecode.com/files/nautilussvn_%{version}-beta1-2.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

#BuildArch: noarch
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: nautilus-python-devel = 0.5.0
BuildRequires: pysvn
BuildRequires: neon-devel
BuildRequires: pygtk2-devel
BuildRequires: python-devel
BuildRequires: subversion-devel >= 1.4.6
Requires: meld
Requires: nautilus-python = 0.5.0
Requires: neon 
Requires: python 
Requires: python-configobj
Requires: subversion >= 1.4.6

Conflicts: rabbitvcs

%description
TortoiseSVN-like GUI integration for Subversion and Nautilus.

%prep
%setup

%build
CFLAGS="%{optflags}" %{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
CFLAGS="%{optflags}" %{__python} setup.py install --root="%{buildroot}" --prefix="%{_prefix}"

%{__rm} -rf %{buildroot}%{_defaultdocdir}/nautilussvn

%{__chmod} 0755 %{buildroot}%{_datadir}/nautilussvn/do-nautilussvn-restart-nautilus

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS COPYING CREDITS MAINTAINERS README THANKS
%{python_sitearch}/*
%{_bindir}/*
%dir %{nautilus_extensiondir}
%{nautilus_extensiondir}/*
%dir %{_iconsbasedir}/scalable/actions/
%{_iconsbasedir}/scalable/actions/*
%dir %{_iconsbasedir}/scalable/emblems/
%{_iconsbasedir}/scalable/emblems/*
%{_iconsscaldir}/*
%{_datadir}/nautilussvn
%dir %{_datadir}/locale/de/LC_MESSAGES/
%{_datadir}/locale/de/LC_MESSAGES/*
%dir %{_datadir}/locale/en_US/LC_MESSAGES/
%{_datadir}/locale/en_US/LC_MESSAGES/*
%dir %{_datadir}/locale/fr_FR/LC_MESSAGES/
%{_datadir}/locale/fr_FR/LC_MESSAGES/*

%changelog
* Thu Oct 08 2009 Steve Huff <shuff@vecna.org> - 0.12beta1_2-1
- Initial package.

