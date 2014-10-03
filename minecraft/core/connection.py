# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import errno
import socket
import select
import logging

from . import exceptions


logger = logging.getLogger(__name__)


class Connection(object):
    def __init__(self, host, port):
        """
        TCP socket connection to a Minecraft Pi game. Default port is 4711.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((host, port))
        except socket.error as e:
            if e.errno != errno.ECONNREFUSED:
                # Not the error we are looking for, re-raise
                raise e
            msg = 'Could not connect to Minecraft server at %s:%s (connection refused).'
            raise exceptions.ConnectionError(msg % (host, port))

        self.last_sent = ''

    def drain(self):
        """
        Drain the socket of incoming data.
        """
        while True:
            readable, _, _ = select.select([self.socket], [], [], 0.0)
            if not readable:
                break
            data = self.socket.recv(1500)
            logger.debug('Drained data: <%s>', data.strip())
            logger.debug('Last message: <%s>', self.last_sent.strip())

    def send(self, func, *args):
        """
        Send data. Note that a trailing newline '\n' is added here.
        """
        s = '%s(%s)\n' % (func, ','.join(map(str, args)))
        self.drain()
        self.last_sent = s
        self.socket.sendall(s.encode('ascii'))
        logger.info('Sent: %s', s)

    def receive(self):
        """
        Receive data. Note that the trailing newline '\n' is trimmed.
        """
        s = self.socket.makefile('r').readline().rstrip('\n')
        logger.info('Read: %s', s)
        if s == 'Fail':
            raise exceptions.APIError('%s failed' % self.last_sent.strip())
        return s

    def send_receive(self, func, *args):
        """
        Send and receive data.
        """
        self.send(func, *args)
        return self.receive()
