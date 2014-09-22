# README

[Minecraft: Pi Edition](http://pi.minecraft.net/) is awesome.

However it uses Python 2. We're moving it to Python 3 (without any official approval) and offering it for download here.

We hope this makes people's lives easier.


## Goals
* [x] Python 3
* [ ] TESTS (pytest, tox, flake8, coverage)
* [ ] More intuitive API focusing on getting some mining done and hiding implementation details
* [ ] Backwards compatibility with the existing codebase (with __init__ foo)
* [ ] Connection backends (socket, in memory for testing)
* [ ] Clever socket usage so disconnects can be dealt with
* [ ] Make the code base more readable and thus maintainable
* [ ] A CI test suite running an rPi emulator (with Travis)
* [ ] Improve code documentation both in the code base and with a RTD page
