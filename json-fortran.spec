%define debug_package %{nil}

Name:           json-fortran
Version:        8.2.5
Release:        1%{?dist}
Summary:        A Modern Fortran JSON API

License:        BSD
Source0:        https://github.com/jacobwilliams/json-fortran/archive/%{version}.tar.gz
 
BuildRequires:  gcc-gfortran
BuildRequires:  cmake
BuildRequires:  python3-pip
BuildRequires:  python3-ford
BuildRequires:  python3-fobis.py

%description
A user-friendly, thread-safe, and object-oriented API for reading and writing JSON files, written in modern Fortran.

%prep
%setup -q -n %{name}-%{version}

%build
./build.sh

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/lib/
mkdir -p %{buildroot}/usr/include/

cp lib/libjsonfortran.a %{buildroot}/usr/lib/
cp lib/*.mod %{buildroot}/usr/include/

%files
%license LICENSE
%doc README.md
/usr/include/*.mod
/usr/lib/libjsonfortran.a

%changelog
* Tue Dec 14 2021 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 8.2.5-1
- Initial package.
