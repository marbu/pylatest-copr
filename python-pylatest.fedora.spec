# Created by pyp2rpm-3.2.2
%global pypi_name pylatest

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        1%{?dist}
Summary:        Testcase description management tools

License:        GPLv3
URL:            http://gitlab.com/mbukatov/pylatest/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Pylatest project consists of set of Docutils/Sphinx extensions and related
tools which allows you to:* Write a description of a test case using
reStructuredText syntax. * Maintain test case description as Sphinx project. *
Include this description into a python source code directly, where it can be
split into individual sections or actions to be performed, so that the
description and test...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-docutils
Requires:       python-lxml
Requires:       python-sphinx >= 1.6.0
Requires:       python-setuptools
%description -n python2-%{pypi_name}
Pylatest project consists of set of Docutils/Sphinx extensions and related
tools which allows you to:* Write a description of a test case using
reStructuredText syntax. * Maintain test case description as Sphinx project. *
Include this description into a python source code directly, where it can be
split into individual sections or actions to be performed, so that the
description and test...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-docutils
Requires:       python3-lxml
Requires:       python3-sphinx >= 1.6.0
Requires:       python3-setuptools
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
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install
cp %{buildroot}/%{_bindir}/pylatest-template %{buildroot}/%{_bindir}/pylatest-template-%{python3_version}
ln -s %{_bindir}/pylatest-template-%{python3_version} %{buildroot}/%{_bindir}/pylatest-template-3
cp %{buildroot}/%{_bindir}/pylatest-rst2html %{buildroot}/%{_bindir}/pylatest-rst2html-%{python3_version}
ln -s %{_bindir}/pylatest-rst2html-%{python3_version} %{buildroot}/%{_bindir}/pylatest-rst2html-3
cp %{buildroot}/%{_bindir}/pylatest-rst2pseudoxml %{buildroot}/%{_bindir}/pylatest-rst2pseudoxml-%{python3_version}
ln -s %{_bindir}/pylatest-rst2pseudoxml-%{python3_version} %{buildroot}/%{_bindir}/pylatest-rst2pseudoxml-3
cp %{buildroot}/%{_bindir}/pylatest-quickstart %{buildroot}/%{_bindir}/pylatest-quickstart-%{python3_version}
ln -s %{_bindir}/pylatest-quickstart-%{python3_version} %{buildroot}/%{_bindir}/pylatest-quickstart-3
cp %{buildroot}/%{_bindir}/pylatest-preview %{buildroot}/%{_bindir}/pylatest-preview-%{python3_version}
ln -s %{_bindir}/pylatest-preview-%{python3_version} %{buildroot}/%{_bindir}/pylatest-preview-3
cp %{buildroot}/%{_bindir}/py2pylatest %{buildroot}/%{_bindir}/py2pylatest-%{python3_version}
ln -s %{_bindir}/py2pylatest-%{python3_version} %{buildroot}/%{_bindir}/py2pylatest-3
cp %{buildroot}/%{_bindir}/pylatest-rst2htmlplain %{buildroot}/%{_bindir}/pylatest-rst2htmlplain-%{python3_version}
ln -s %{_bindir}/pylatest-rst2htmlplain-%{python3_version} %{buildroot}/%{_bindir}/pylatest-rst2htmlplain-3

%py2_install
cp %{buildroot}/%{_bindir}/pylatest-template %{buildroot}/%{_bindir}/pylatest-template-%{python2_version}
ln -s %{_bindir}/pylatest-template-%{python2_version} %{buildroot}/%{_bindir}/pylatest-template-2
cp %{buildroot}/%{_bindir}/pylatest-rst2html %{buildroot}/%{_bindir}/pylatest-rst2html-%{python2_version}
ln -s %{_bindir}/pylatest-rst2html-%{python2_version} %{buildroot}/%{_bindir}/pylatest-rst2html-2
cp %{buildroot}/%{_bindir}/pylatest-rst2pseudoxml %{buildroot}/%{_bindir}/pylatest-rst2pseudoxml-%{python2_version}
ln -s %{_bindir}/pylatest-rst2pseudoxml-%{python2_version} %{buildroot}/%{_bindir}/pylatest-rst2pseudoxml-2
cp %{buildroot}/%{_bindir}/pylatest-quickstart %{buildroot}/%{_bindir}/pylatest-quickstart-%{python2_version}
ln -s %{_bindir}/pylatest-quickstart-%{python2_version} %{buildroot}/%{_bindir}/pylatest-quickstart-2
cp %{buildroot}/%{_bindir}/pylatest-preview %{buildroot}/%{_bindir}/pylatest-preview-%{python2_version}
ln -s %{_bindir}/pylatest-preview-%{python2_version} %{buildroot}/%{_bindir}/pylatest-preview-2
cp %{buildroot}/%{_bindir}/py2pylatest %{buildroot}/%{_bindir}/py2pylatest-%{python2_version}
ln -s %{_bindir}/py2pylatest-%{python2_version} %{buildroot}/%{_bindir}/py2pylatest-2
cp %{buildroot}/%{_bindir}/pylatest-rst2htmlplain %{buildroot}/%{_bindir}/pylatest-rst2htmlplain-%{python2_version}
ln -s %{_bindir}/pylatest-rst2htmlplain-%{python2_version} %{buildroot}/%{_bindir}/pylatest-rst2htmlplain-2


%files -n python2-%{pypi_name}
%doc README.rst
%{_bindir}/pylatest-template
%{_bindir}/pylatest-template-2
%{_bindir}/pylatest-template-%{python2_version}
%{_bindir}/pylatest-rst2html
%{_bindir}/pylatest-rst2html-2
%{_bindir}/pylatest-rst2html-%{python2_version}
%{_bindir}/pylatest-rst2pseudoxml
%{_bindir}/pylatest-rst2pseudoxml-2
%{_bindir}/pylatest-rst2pseudoxml-%{python2_version}
%{_bindir}/pylatest-quickstart
%{_bindir}/pylatest-quickstart-2
%{_bindir}/pylatest-quickstart-%{python2_version}
%{_bindir}/pylatest-preview
%{_bindir}/pylatest-preview-2
%{_bindir}/pylatest-preview-%{python2_version}
%{_bindir}/py2pylatest
%{_bindir}/py2pylatest-2
%{_bindir}/py2pylatest-%{python2_version}
%{_bindir}/pylatest-rst2htmlplain
%{_bindir}/pylatest-rst2htmlplain-2
%{_bindir}/pylatest-rst2htmlplain-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/pylatest-template-3
%{_bindir}/pylatest-template-%{python3_version}
%{_bindir}/pylatest-rst2html-3
%{_bindir}/pylatest-rst2html-%{python3_version}
%{_bindir}/pylatest-rst2pseudoxml-3
%{_bindir}/pylatest-rst2pseudoxml-%{python3_version}
%{_bindir}/pylatest-quickstart-3
%{_bindir}/pylatest-quickstart-%{python3_version}
%{_bindir}/pylatest-preview-3
%{_bindir}/pylatest-preview-%{python3_version}
%{_bindir}/py2pylatest-3
%{_bindir}/py2pylatest-%{python3_version}
%{_bindir}/pylatest-rst2htmlplain-3
%{_bindir}/pylatest-rst2htmlplain-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Apr 16 2018 Martin Bukatovic <martin.bukatovic@gmail.com> - 0.1.2-1
- Build for upstream version 0.1.2

* Mon Apr 16 2018 Martin Bukatovic <martin.bukatovic@gmail.com> - 0.1.1-1
- Initial package.
