%define	module	vcs
%define name	python-%{module}
%define version	0.2.1
%define release	%mkrel 1

Summary:	Version control system management abstraction layer for Python
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/v/%{module}/%{module}-%{version}.tar.gz
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
 
%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc README.rst docs/build/html/
