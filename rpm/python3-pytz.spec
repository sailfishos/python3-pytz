Summary:       Pytz
Name:          python3-pytz
Version:       0
Release:       1
License:       MIT
Source0:       %{name}-%{version}.tar.gz
URL:           https://github.com/sailfishos/python3-pytz
Patch0:        0001-Use-system-zoneinfo.patch

BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: rsync

%description
pytz brings the Olson tz database into Python

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%make_build -j1 build
cd src
%py3_build

%install
cd src
%py3_install
rm -r %{buildroot}%{python3_sitelib}/pytz/zoneinfo

%files
%defattr (-,root,root,-)
%license LICENSE.txt
%{python3_sitelib}/pytz/
%{python3_sitelib}/*.egg-info

