# Created by pyp2rpm-3.3.2
%global pypi_name pylatest

Name:           python-%{pypi_name}
Version:        0.1.3
Release:        3%{?dist}
Summary:        Testcase description management tools

License:        GPLv3
URL:            http://gitlab.com/mbukatov/pylatest/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx) >= 1.6.0

%description
Pylatest project consists of set of Docutils/Sphinx extensions and related
tools which allows you to:* Write a description of a test case using
reStructuredText syntax. * Maintain test case description as Sphinx project. *
Include this description into a python source code directly, where it can be
split into individual sections or actions to be performed, so that the
description and test...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(docutils)
Requires:       python3dist(lxml)
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx) >= 1.6.0
Requires:       man-db
%description -n python3-%{pypi_name}
Pylatest project consists of set of Docutils/Sphinx extensions and related
tools which allows you to:* Write a description of a test case using
reStructuredText syntax. * Maintain test case description as Sphinx project. *
Include this description into a python source code directly, where it can be
split into individual sections or actions to be performed, so that the
description and test...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/py2pylatest
%{_bindir}/pylatest-preview
%{_bindir}/pylatest-rst2html
%{_bindir}/pylatest-rst2htmlplain
%{_bindir}/pylatest-rst2pseudoxml
%{_bindir}/pylatest-template
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Sep 18 2018 Martin Bukatovic <martin.bukatovic@gmail.com> - 0.1.3-3
- Quote rpm macros referenced in specfile changelog

* Mon Sep 17 2018 Martin Bukatovic <martin.bukatovic@gmail.com> - 0.1.3-2
- Replace %%pypi_source macro with PyPI url for Source0 field

* Mon Sep 17 2018 Martin Bukatovic <martin.bukatovic@gmail.com> - 0.1.3-1
- Build for upstream version 0.1.3
- Regenerate specfile using pyp2rpm-3.3.2
- Use %%pypi_source macro as Source0

* Wed Apr 18 2018 Martin Bukatovic <martin.bukatovic@gmail.com> - 0.1.2-2
- Add man as a dependency
- Tweak package description

* Mon Apr 16 2018 Martin Bukatovic <martin.bukatovic@gmail.com> - 0.1.2-1
- Build for upstream version 0.1.2

* Mon Apr 16 2018 Martin Bukatovic <martin.bukatovic@gmail.com> - 0.1.1-1
- Initial package.
