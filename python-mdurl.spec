Summary:	Markdown URL utilities
Name:		python-mdurl
Version:	0.1.2
Release:	2
Group:		Development/Python
License:	MIT
URL:		https://github.com/executablebooks/mdurl
#Source0:	https://github.com/executablebooks/mdurl/archive/%{version}/mdurl-%{version}.tar.gz
Source0:	https://pypi.io/packages/source/m/mdurl/mdurl-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

BuildArch:	noarch

%description
This is a Python port of the JavaScript mdurl package.

%files
%license LICENSE
%doc README.md
%{py_sitedir}/mdurl
%{py_sitedir}/mdurl-*.*-info

#--------------------------------------------------------------------

%prep
%autosetup -n mdurl-%{version}

%build
%py_build
 
%install
%py_install

