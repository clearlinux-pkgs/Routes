#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Routes
Version  : 2.5.1
Release  : 48
URL      : https://files.pythonhosted.org/packages/62/01/1504b710f68840f4152d460a4ffbc6b8265485b636235ddd72a8dfe686ae/Routes-2.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/01/1504b710f68840f4152d460a4ffbc6b8265485b636235ddd72a8dfe686ae/Routes-2.5.1.tar.gz
Summary  : Routing Recognition and Generation Tools
Group    : Development/Tools
License  : MIT
Requires: Routes-license = %{version}-%{release}
Requires: Routes-python = %{version}-%{release}
Requires: Routes-python3 = %{version}-%{release}
Requires: repoze.lru
Requires: six
BuildRequires : WebTest
BuildRequires : buildreq-distutils3
BuildRequires : coverage-python
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : pip
BuildRequires : repoze.lru
BuildRequires : repoze.lru-python
BuildRequires : six
BuildRequires : soupsieve-python
BuildRequires : webob-python
BuildRequires : webtest-python

%description
URL's to Controllers/Actions and generating URL's. Routes makes it easy to
        create pretty and concise URL's that are RESTful with little effort.
        
        Speedy and dynamic URL generation means you get a URL with minimal cruft
        (no big dangling query args). Shortcut features like Named Routes cut down
        on repetitive typing.

%package license
Summary: license components for the Routes package.
Group: Default

%description license
license components for the Routes package.


%package python
Summary: python components for the Routes package.
Group: Default
Requires: Routes-python3 = %{version}-%{release}
Provides: routes-python

%description python
python components for the Routes package.


%package python3
Summary: python3 components for the Routes package.
Group: Default
Requires: python3-core
Provides: pypi(routes)
Requires: pypi(repoze.lru)
Requires: pypi(six)

%description python3
python3 components for the Routes package.


%prep
%setup -q -n Routes-2.5.1
cd %{_builddir}/Routes-2.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636042483
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . soupsieve
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Routes
cp %{_builddir}/Routes-2.5.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/Routes/9307dc7f8ab43367bf5ed7b3b5173523f44fcca2
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} soupsieve
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Routes/9307dc7f8ab43367bf5ed7b3b5173523f44fcca2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
