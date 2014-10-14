README
======

.. image:: https://secure.travis-ci.org/py3minepi/py3minepi.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/py3minepi/py3minepi

.. image:: https://coveralls.io/repos/py3minepi/py3minepi/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/py3minepi/py3minepi

.. image:: https://landscape.io/github/py3minepi/py3minepi/master/landscape.png
    :alt: Code Health
    :target: https://landscape.io/github/py3minepi/py3minepi


`Minecraft: Pi Edition <http://pi.minecraft.net/>`__ is awesome.

However it uses Python 2. We're moving it to Python 3 (without any official
approval) and offering it for download here.

We hope this makes people's lives easier.


Goals
-----

- [x] Python 3
- [ ] TESTS (pytest, tox, flake8, coverage)
- [ ] More intuitive API focusing on getting some mining done and hiding implementation details
- [ ] Backwards compatibility with the existing codebase (with `__init__` foo) so existing scripts will continue to work
- [ ] Connection backends (socket, in memory for testing)
- [ ] Clever socket usage so disconnects can be dealt with
- [ ] Make the code base more readable and thus maintainable
- [ ] A CI test suite running an rPi emulator (with Travis)
- [ ] Improve code documentation both in the code base and with a RTD page
- [ ] Find missing functions that are in the java API but not described in the python API


Coding Guidelines
-----------------

All code (except legacy API compatibility code) should adhere to `PEP8
<http://legacy.python.org/dev/peps/pep-0008/>`_ with some exceptions:

- Try to keep your line length below 80, but if it looks better then use up to
  99 characters per line.
- You can ignore the following three PEP8 rules: E126 (continuation line
  over-indented for hanging indent), E127 (continuation line over-indented for
  visual indent), E128 (continuation line under-indented for visual indent).

You can check the code style for example by using `flake8
<https://pypi.python.org/pypi/flake8>`_.

Some other things you should keep in mind:

- Function names should mirror ingame commands where possible.
- Group imports into three groups: First stdlib imports, then third party
  imports, then local imports. Put an empty line between each group.
- Backwards compatibility must be maintained unless you have a very compelling
  reason.
- KISS!

For backwards compatibility with Python 2, please insert this header in every
Python module::

    # -*- coding: utf-8 -*-
    from __future__ import print_function, division, absolute_import, unicode_literals


Testing
-------

Testing for py3minepi is set up using `Tox <http://tox.readthedocs.org/>`_ and
`pytest <http://pytest.org/>`_. Violations of the `coding guidelines
<#coding-guidelines>`__ are counted as test fails.

The only requirement to run the tests is tox::

    $ pip install tox

**Running tests**

To run the tests on all supported Python versions, simply issue ::

    $ tox

To test only a single Python version, use the ``-e`` parameter::

    $ tox -e py32

To see the test coverage, use the ``cov`` testenv (which uses Python 3.2 by
default)::

    $ tox -e cov

All Python versions you need to test on need to be installed of course.


Links
-----

- `Raspberry Pi <http://www.raspberrypi.org/>`_
- `Minecraft Pi <http://pi.minecraft.net/>`_
- `Minecraft Pi Usage page <http://www.raspberrypi.org/documentation/usage/minecraft/>`_
- `Original API reference <http://www.stuffaboutcode.com/p/minecraft-api-reference.html>`_
- `Martin O'Hanlon GitHub <https://github.com/martinohanlon>`_ (useful test projects)
