#
# Conditional build:
%bcond_without	python2		# Python 2.x module
%bcond_with	python3		# Python 3.x module
#
%define	module	repoguard
#
Summary:	A framework for Subversion commit hooks
Name:		python-repoguard
Version:	0.2.0
Release:	0.1
License:	APL
Group:		Development/Version Control
Source0:	http://repoguard.tigris.org/files/documents/6497/48735/repoguard-%{version}.tar
# Source0-md5:	b7036d436e819576917daa3bca0f2482
URL:		http://repoguard.tigris.org/
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-modules
Requires:	python
Requires:	python-configobj
%endif
%if %{with python3}
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
BuildRequires:	python3-modules
%endif
BuildRequires:	rpm-pythonprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RepoGuard is an advanced validation framework with built-in
integrations for several common version control systems. It is the
successor of the SVNChecker framework.

%package -n	python3-%{module}
Summary:	A framework for Subversion commit hooks
Group:		Libraries/Python
Requires:	python3
Requires:	python3-configobj

%description -n python3-%{module}
RepoGuard is an advanced validation framework with built-in
integrations for several common version control systems. It is the
successor of the SVNChecker framework.

%prep
%setup  -q -n repoguard-%{version}

%build
%if %{with python2}
%{__python} ./setup.py build --build-base py2
%endif
%if %{with python3}
%{__python3} ./setup.py build --build-base py3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python-%{module}-%{version}
%{__python} ./setup.py build \
	--build-base py2 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%if %{with python3}
install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%{__python3} ./setup.py build \
	--build-base py3 \
	install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES README
%{_examplesdir}/python-%{module}-%{version}
%attr(755,root,root) %{_bindir}/repoguard
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/*egg-info
%{py_sitescriptdir}/*nspkg.pth
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%endif
