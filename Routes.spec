#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Routes
Version  : 2.4.1
Release  : 27
URL      : http://pypi.debian.net/Routes/Routes-2.4.1.tar.gz
Source0  : http://pypi.debian.net/Routes/Routes-2.4.1.tar.gz
Summary  : Routing Recognition and Generation Tools
Group    : Development/Tools
License  : MIT
Requires: Routes-python
Requires: repoze.lru
Requires: six
BuildRequires : WebTest
BuildRequires : coverage-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : repoze.lru
BuildRequires : repoze.lru-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : webob-python

%description
routes-logo-haas.svg
Routes logo by Christoph Boehme, 2009.

%package python
Summary: python components for the Routes package.
Group: Default
Provides: routes-python

%description python
python components for the Routes package.


%prep
%setup -q -n Routes-2.4.1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1492438718
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1492438718
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
