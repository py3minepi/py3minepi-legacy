# -*- coding: utf-8 -*-
"""
Exceptions to be used in py3minepi.
"""
from __future__ import print_function, division, absolute_import, unicode_literals


class ConnectionError(RuntimeError):
    """
    Raised if something goes wrong with the connection.
    """
    pass


class APIError(RuntimeError):
    """
    Can be used if there are problems with the API.
    """
    pass


class ValidationError(ValueError):
    """
    Used for validation purposes.
    """
    pass
