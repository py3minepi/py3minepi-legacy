# -*- coding: utf-8 -*-
"""
Low level Minecraft API client library.

This is a re-implementation of a low level client library for the Minecraft
API. It tries to stay close to the API calls. Basic data types are preferred
over custom types in here.

"""
from __future__ import print_function, division, absolute_import, unicode_literals

import logging

from .connection import Connection


logger = logging.getLogger(__name__)


class Command(object):
    """
    The command base class.
    """
    _func_prefix = ''

    def __init__(self, connection):
        self._conn = connection

    def _send(self, func, *args):
        full_func = '%s.%s' % (self._func_prefix, func)
        self._conn.send(full_func, *args)

    def _send_receive(self, func, *args):
        full_func = '%s.%s' % (self._func_prefix, func)
        return self._conn.send_receive(full_func, *args)


class WorldCommand(Command):
    _func_prefix = 'world'

    def get_block(self, x, y, z):
        value = self._send_receive('getBlock', x, y, z)
        return int(value)

    def set_block(self, x, y, z, block_type):
        self._send('setBlock', x, y, z, block_type)

    def set_blocks(self, x1, y1, z1, x2, y2, z2, block_type):
        self._send('setBlocks', x1, y1, z1, x2, y2, z2, block_type)

    def get_height(self, x, z):
        value = self._send_receive('getHeight', x, z)
        return int(value)

    def save_checkpoint(self):
        self._send('checkpoint.save')

    def restore_checkpoint(self):
        self._send('checkpoint.restore')

    def setting(self):
        # TODO what does this do?
        pass


class ChatCommand(Command):
    _func_prefix = 'chat'

    def say(self, message):
        self._send('post', message)
        pass


class PlayerCommand(Command):
    _func_prefix = 'player'

    def get_tile(self):
        value = self._send_receive('getTile')
        return [int(x) for x in value.split(',')]

    def set_tile(self, x, y, z):
        self._send('setTile', x, y, z)

    def get_pos(self):
        value = self._send_receive('getPos')
        return [float(x) for x in value.split(',')]

    def set_pos(self, x, y, z):
        self._send('setPos', x, y, z)


class CameraCommand(Command):
    _func_prefix = 'camera.mode'

    def set_normal(self):
        self._send('setNormal')

    def set_third_person(self):
        self._send('setThirdPerson')

    def set_fixed(self):
        self._send('setFixed')

    def set_pos(self, x, y, z):
        self._send('setPos', x, y, z)


class Minecraft(object):

    def __init__(self, host='127.0.0.1', port=4711):
        logger.info('Initializing connection to %s:%d...', host, port)
        self.conn = Connection(host, port)
        logger.info('Loading world commands...')
        self.world = WorldCommand(self.conn)
        logger.info('Loading chat commands...')
        self.chat = ChatCommand(self.conn)
        logger.info('Loading player commands...')
        self.player = PlayerCommand(self.conn)
        logger.info('Loading camera commands...')
        self.camera = CameraCommand(self.conn)
