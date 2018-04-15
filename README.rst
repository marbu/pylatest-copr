=============================
 Pylatest Specfiles for COPR
=============================

Specfiles for Fedora builds of `Pylatest`_, created with
the help of `pyp2rpm`_ tool.

Builds are available in `marbu/pylatest copr
<https://copr.fedorainfracloud.org/coprs/marbu/pylatest/>`_.


Manual Build Process on Fedora with Mock
========================================

First of all, you need a `sdist tarball`_. You can either download one for the
latest stable release from PyPI via pip::

    $ pip download pylatest --no-deps -d .

Or you can generate one yourself from the sources like this::

    $ cd ~/projects/
    $ git clone https://gitlab.com/mbukatov/pylatest.git
    $ git checkout v0.1.1
    $ python3 setup.py sdist

Copy the specfile and sdist tarball into rpmbuild directory tree::

    $ cp ~/projects/pylatest/dist/pylatest-0.1.1.tar.gz ~/rpmbuild/SOURCES
    $ cp python-pylatest.fedora.spec ~/rpmbuild/SPECS

So that we can generate the source rpm::

    $ cd ~/rpmbuild/SPECS
    $ rpmbuild -bs python-pylatest.fedora.spec
    $ ls ~/rpmbuild/SRPMS
    python-pylatest-0.1.1-1.fc26.src.rpm

Which we can build it locally with `mock`_::

    $ cd ~/rpmbuild/SPECS
    $ mock -r fedora-26-x86_64 --rebuild python-pylatest-0.1.1-1.fc26.src.rpm

Note: mock does the build in clean chroot enviroment and it's used both by koji
and copr.

When the build finishes with success, the rpm packages can be found in the
result directory::

    $ ls /var/lib/mock/fedora-26-x86_64/result/
    build.log
    hw_info.log
    installed_pkgs.log
    python-pylatest-0.1.1-1.fc26.src.rpm
    python2-pylatest-0.1.1-1.fc26.noarch.rpm
    python3-pylatest-0.1.1-1.fc26.noarch.rpm
    root.log
    state.log


Building with Copr
==================

Assuming we aready have a `Copr`_ project for the package, and the `copr-cli
tool`_ has been configured, we can just upload the source rpm file into the
project::

    $ copr-cli build -r fedora-25-x86_64 -r fedora-26-x86_64 pylatest ~/rpmbuild/SRPMS/python-pylatest-0.1.1-1.fc26.src.rpm


.. _`Pylatest`: https://gitlab.com/mbukatov/pylatest/
.. _`pyp2rpm`: https://github.com/fedora-python/pyp2rpm
.. _`sdist tarball`: https://packaging.python.org/glossary/?highlight=sdist#term-source-distribution-or-sdist
.. _`mock`: https://github.com/rpm-software-management/mock/wiki#using-mock-outside-your-git-sandbox
.. _`Copr`: https://developer.fedoraproject.org/deployment/copr/about.html
.. _`copr-cli tool`: https://developer.fedoraproject.org/deployment/copr/copr-cli.html
