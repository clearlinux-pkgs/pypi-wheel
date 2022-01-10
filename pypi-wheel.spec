#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-wheel
Version  : 0.37.1
Release  : 98
URL      : https://files.pythonhosted.org/packages/c0/6c/9f840c2e55b67b90745af06a540964b73589256cb10cc10057c87ac78fc2/wheel-0.37.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/6c/9f840c2e55b67b90745af06a540964b73589256cb10cc10057c87ac78fc2/wheel-0.37.1.tar.gz
Summary  : A built-package format for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-wheel-bin = %{version}-%{release}
Requires: pypi-wheel-license = %{version}-%{release}
Requires: pypi-wheel-python = %{version}-%{release}
Requires: pypi-wheel-python3 = %{version}-%{release}
Requires: pypi(keyring)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
=====
        
        This library is the reference implementation of the Python wheel packaging
        standard, as defined in `PEP 427`_.

%package bin
Summary: bin components for the pypi-wheel package.
Group: Binaries
Requires: pypi-wheel-license = %{version}-%{release}

%description bin
bin components for the pypi-wheel package.


%package license
Summary: license components for the pypi-wheel package.
Group: Default

%description license
license components for the pypi-wheel package.


%package python
Summary: python components for the pypi-wheel package.
Group: Default
Requires: pypi-wheel-python3 = %{version}-%{release}

%description python
python components for the pypi-wheel package.


%package python3
Summary: python3 components for the pypi-wheel package.
Group: Default
Requires: python3-core
Provides: pypi(wheel)

%description python3
python3 components for the pypi-wheel package.


%prep
%setup -q -n wheel-0.37.1
cd %{_builddir}/wheel-0.37.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641842867
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-wheel
cp %{_builddir}/wheel-0.37.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-wheel/53aa128e9d6387e9bb9d945fdcbf1ab4d003baed
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wheel

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-wheel/53aa128e9d6387e9bb9d945fdcbf1ab4d003baed

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
