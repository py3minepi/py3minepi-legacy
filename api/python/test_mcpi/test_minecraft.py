'''Tests for the legacy minecraft module.
'''

from mcpi.minecraft import Minecraft
import mcpi.connection

# We monkey-patch socket and select in connection.py.  This allows us
# to 'listen to the wire' without the trouble of setting up a real
# socket server.

class DummySocket:
    '''Dummy socket.socket class.
    '''
    def __init__(self, address, port):
        self._sent = []

    def connect(self, address_port):
        pass

    def sendall(self, s):
        self._sent.append(s)


class DummySocketModule:
    '''Dummy socket module.
    '''
    AF_INET = SOCK_STREAM = None
    socket = DummySocket


class DummySelectModule:
    '''Dummy select module.
    '''
    def select(self, *args):
        return False, None, None


# Do the monkey patch.  Affects only connection.py.
mcpi.connection.socket = DummySocketModule()
mcpi.connection.select = DummySelectModule()

# Create the 'test fixture'.
mc = Minecraft.create()
sent = mc.conn.socket._sent


def test_postToChat():

    # This succeeds.  Good.
    mc.postToChat('hi')
    assert sent[-1] == 'chat.post(hi)\n'

    # This should fail but does not.  Bad.
    mc.postToChat('lookout)\ngotcha(')
    assert sent[-1] == 'chat.post(lookout)\ngotcha()\n'


def test_setPos():

    # Here we get what we expect.
    mc.player.setPos(3, 4, 5, 6)
    assert sent[-1] == 'player.setPos(3,4,5,6)\n'
