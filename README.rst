README
======

.. image:: https://secure.travis-ci.org/py3minepi/py3minepi.png?branch=master
    :alt: Build status
    :target: https://travis-ci.org/py3minepi/py3minepi

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

Links
-----

- `Raspberry Pi <http://www.raspberrypi.org/>`_
- `Minecraft Pi <http://pi.minecraft.net/>`_
- `Minecraft Pi Usage page <http://www.raspberrypi.org/documentation/usage/minecraft/>`_
- `Original API reference <http://www.stuffaboutcode.com/p/minecraft-api-reference.html>`_
- `Martin O'Hanlon GitHub <https://github.com/martinohanlon>`_ (useful test projects)
