import socket
import errno
import select
import sys

from . import exceptions
from .util import flatten_parameters_to_string


class RequestError(Exception):
    pass


class Connection:
    """
    Connection to a Minecraft Pi game.
    """
    RequestFailed = "Fail"

    def __init__(self, address, port):
        """
        Initialize TCP socket connection.
        """
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((address, port))
        except socket.error as e:
            if e.errno != errno.ECONNREFUSED:
                # Not the error we are looking for, re-raise
                raise e
            msg = 'Could not connect to Minecraft server at %s:%s (connection refused).'
            raise exceptions.ConnectionError(msg % (address, port))

        self.lastSent = ''

    def drain(self):
        """
        Drains the socket of incoming data.
        """
        while True:
            readable, _, _ = select.select([self.socket], [], [], 0.0)
            if not readable:
                break
            data = self.socket.recv(1500)
            e = 'Drained Data: <{}>\n'.format(data.strip())
            e += 'Last Message: <{}>\n'.format(self.lastSent.strip())
            sys.stderr.write(e)

    def send(self, f, *data):
        """
        Sends data. Note that a trailing newline '\n' is added here.
        """
        s = "%s(%s)\n" % (f, flatten_parameters_to_string(data))

        self._send(s)

    def _send(self, s):
        """
        The actual socket interaction from self.send, extracted for easier mocking
        and testing
        """
        self.drain()
        self.lastSent = s

        self.socket.sendall(s.encode())

    def receive(self):
        """
        Receives data. Note that the trailing newline '\n' is trimmed.
        """
        s = self.socket.makefile("r").readline().rstrip("\n")
        if s == Connection.RequestFailed:
            raise RequestError('{} failed'.format(self.lastSent.strip()))
        return s

    def sendReceive(self, *data):
        """
        Sends and receive data.
        """
        self.send(*data)
        return self.receive()
