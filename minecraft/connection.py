import socket
import select
import sys

""" @author: Aron Nieminen, Mojang AB"""

class RequestError(Exception):
    pass

class Connection:
    """Connection to a Minecraft Pi game"""
    RequestFailed = "Fail"

    def __init__(self, address, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((address, port))
        self.lastSent = ""

    def drain(self):
        """Drains the socket of incoming data"""
        while True:
            readable, _, _ = select.select([self.socket], [], [], 0.0)
            if not readable:
                break
            data = self.socket.recv(1500)
            e =  'Drained Data: <{}>\n'.format(data.strip())
            e += 'Last Message: <{}>\n'.format(self.lastSent.strip())
            sys.stderr.write(e)

    def send(self, f, *data):
        """Sends data. Note that a trailing newline '\n' is added here"""
        flattened_params = ','.join(map(str, itertools.chain.from_iterable(data)))
        s = '{}({})\n'.format(f, flattened_params)
        self.drain()
        self.lastSent = s
        self.socket.sendall(s.encode())

    def receive(self):
        """Receives data. Note that the trailing newline '\n' is trimmed"""
        s = self.socket.makefile("r").readline().rstrip("\n")
        if s == Connection.RequestFailed:
            raise RequestError('{} failed'.format(self.lastSent.strip()))
        return s

    def sendReceive(self, *data):
        """Sends and receive data"""
        self.send(*data)
        return self.receive()
