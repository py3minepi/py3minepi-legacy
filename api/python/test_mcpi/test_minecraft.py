'''Tests for the legacy minecraft module.
'''

from StringIO import StringIO

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
        self._received = ''

    def connect(self, address_port):
        pass

    def sendall(self, s):
        self._sent.append(s)

    def makefile(self, args):

        return StringIO(self._received)


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


# TODO: Improve the test framework.

# Each of these tests below has the following attributes
# * command name
# * arguments
# * sent
# * received
# * return value

# Here's a draft that allow the tests below to be refactored into a
# common framework.  But I've not yet implemented it.
class McTest(tuple):

    def __new__(cls, cmd, argv, sent, received, value):
        return tuple.__new__(cls, [cmd, argv, sent, received, value])

    def run(self):
        pass


# Here's a test.  But we can't run it yet.
# TODO: Maybe allow the test to have a comment or name.
chat_test = McTest(
    'postToChat',
    ['hi'],
    'chat.post(hi)\n',
    None,
    None
)


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


def test_getBlock():

    # The order here is slightly odd.
    mc.conn.socket._received = '5\n'
    assert mc.getBlock(1, 2, 3) == 5
    assert sent[-1] == 'world.getBlock(1,2,3)\n'


def test_setBlocks():

    # I doubt that this is semantically correct.
    mc.setBlocks(1, 2, 3, 4, 5, 6, [])
    assert sent[-1] == 'world.setBlocks(1,2,3,4,5,6)\n'

    # I doubt that this is semantically correct.
    mc.setBlocks(1, 2, 3, 4, 5, 6, list(range(4)))
    assert sent[-1] == 'world.setBlocks(1,2,3,4,5,6,0,1,2,3)\n'
