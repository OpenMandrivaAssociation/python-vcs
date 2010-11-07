%define	module	vcs
%define name	python-%{module}
%define version	0.1.9
%define release	%mkrel 1

Summary:	Version control system management abstraction layer for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
Patch0:		exclude-tests.patch
License:	MIT
Group:		Development/Python
Url:		http://bitbucket.org/marcinkuzminski/vcs/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel, python-setuptools

%description
vcs is a Python library that provides an abstraction layer over
various version control systems.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0
 
%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README.rst docs/build/html/
