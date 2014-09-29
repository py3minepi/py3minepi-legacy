from .connection import Connection
from .vec3 import Vec3
from .event import BlockEvent
from .block import Block
import math
from .util import flatten

""" Minecraft PI low level api v0.1_1

    Note: many methods have the parameter *arg. This solution makes it
    simple to allow different types, and variable number of arguments.
    The actual magic is a mix of flatten_parameters() and __iter__. Example:
    A Cube class could implement __iter__ to work in Minecraft.setBlocks(c, id).

    (Because of this, it's possible to "erase" arguments. CmdPlayer removes
     entityId, by injecting [] that flattens to nothing)

    @author: Aron Nieminen, Mojang AB"""


def intFloor(*args):
    """
    Run math.floor on each argument passed in

    Arguments passed in are expected to be x, y & z coordinates.

    Returns integers (int).
    """
    return map(math.floor, args)

class CmdPositioner:
    """Methods for setting and getting positions"""
    def __init__(self, connection, packagePrefix):
        self.conn = connection
        self.pkg = packagePrefix

    def getPos(self, id):
        """Get entity position (entityId:int) => Vec3"""
        s = self.conn.sendReceive(self.pkg + ".getPos", id)
        return Vec3(*map(float, s.split(",")))

    def setPos(self, id, vector3):
        """Set entity position (entityId:int, x,y,z)"""
        self.conn.send(self.pkg + ".setPos", id, vector3.x, vector3.y, vector3.z)

    def getTilePos(self, id):
        """Get entity tile position (entityId:int) => Vec3"""
        s = self.conn.sendReceive(self.pkg + ".getTile", id)
        return Vec3(*map(float, s.split(",")))

    def setTilePos(self, id, vector3):
        """Set entity tile position (entityId:int, x,y,z)"""
        self.conn.send(self.pkg + ".setTile", id, intFloor(vector3.x, vector3.y, vector3.z))

    def setting(self, setting, status):
        """Set a player setting (setting, status). keys: autojump"""
        self.conn.send(self.pkg + ".setting", setting, 1 if bool(status) else 0)


class CmdEntity(CmdPositioner):
    """Methods for entities"""
    def __init__(self, connection):
        super(CmdEntity, self).__init__(connection, "entity")


class CmdPlayer(CmdPositioner):
    """Methods for the host (Raspberry Pi) player"""
    def __init__(self, connection):
        super(CmdPlayer, self).__init__(connection, "player")
        self.conn = connection

    def getPos(self):
        return CmdPositioner.getPos(self, [])

    def setPos(self, *args):
        return CmdPositioner.setPos(self, [], args)

    def getTilePos(self):
        return CmdPositioner.getTilePos(self, [])

    def setTilePos(self, *args):
        return CmdPositioner.setTilePos(self, [], args)


class CmdCamera:
    def __init__(self, connection):
        self.conn = connection

    def setNormal(self, *args):
        """Set camera mode to normal Minecraft view ([entityId])"""
        self.conn.send("camera.mode.setNormal", args)

    def setFixed(self):
        """Set camera mode to fixed view"""
        self.conn.send("camera.mode.setFixed")

    def setFollow(self, *args):
        """Set camera mode to follow an entity ([entityId])"""
        self.conn.send("camera.mode.setFollow", args)

    def setPos(self, *args):
        """Set camera entity position (x,y,z)"""
        self.conn.send("camera.setPos", args)


class CmdEvents:
    """Events"""
    def __init__(self, connection):
        self.conn = connection

    def clearAll(self):
        """Clear all old events"""
        self.conn.send("events.clear")

    def pollBlockHits(self):
        """Only triggered by sword => [BlockEvent]"""
        s = self.conn.sendReceive("events.block.hits")
        events = [e for e in s.split("|") if e]
        return [BlockEvent.Hit(*map(int, e.split(","))) for e in events]


class Minecraft:
    """The main class to interact with a running instance of Minecraft Pi."""
    def __init__(self, address="localhost", port=4711):
        self._conn = Connection(address, port)

        self.camera = CmdCamera(self._conn)
        self.entity = CmdEntity(self._conn)
        self.player = CmdPlayer(self._conn)
        self.events = CmdEvents(self._conn)

        self.getHeight = self.getGroundHeight
    """
    Messy right now, but you can't refactor without breaking some eggs
    """

    def getBlock(self, vector3):
        """Get block (x,y,z) => id:int"""
        args = [vector3.x, vector3.y, vector3.z]
        return int(self._conn.sendReceive("world.getBlock", intFloor(args)))

    def getBlockWithData(self, vector3):
        """Get block with data (x,y,z) => Block"""
        args = [vector3.x, vector3.y, vector3.z]
        ans = self._conn.sendReceive("world.getBlockWithData", intFloor(args))
        return Block(*map(int, ans.split(",")))

        """
        @TODO (What?)
        """
    def getBlocks(self, vector3_1, vector3_2):
        """Get a cuboid of blocks (x0,y0,z0,x1,y1,z1) => [id:int]"""
        args = [vector3_1.x, vector3_1.y, vector3_1.z, vector3_2.x, vector3_2.y, vector3_2.z] #cringe
        return int(self._conn.sendReceive("world.getBlocks", intFloor(args)))

    def setBlock(self, vector3, blockType, data=None):
        """Set block (x,y,z,id,[data])"""
        args = [vector3.x, vector3.y, vector3.z, blockType]
        if data:
            args.append(data)
        self._conn.send("world.setBlock", intFloor(args))


    def setBlocks(self, *args): #leaving thisone alone for now
        """Set a cuboid of blocks (x0,y0,z0,x1,y1,z1,id,[data])"""
        self._conn.send("world.setBlocks", intFloor(args))


    def getGroundHeight(self, x,z):
        """Get the height of the world (x,z) => int"""

        return int(self._conn.sendReceive("world.getHeight", intFloor([x,z])))

    def getPlayerEntityIds(self):
        """Get the entity ids of the connected players => [id:int]"""
        ids = self._conn.sendReceive("world.getPlayerIds")
        return list(map(int, ids.split("|")))

    def saveCheckpoint(self):
        """Save a checkpoint that can be used for restoring the world"""
        self._conn.send("world.checkpoint.save")

    def restoreCheckpoint(self):
        """Restore the world state to the checkpoint"""
        self._conn.send("world.checkpoint.restore")

    def postToChat(self, msg):
        """Post a message to the game chat"""
        self._conn.send("chat.post", msg)

    def setting(self, setting, status):
        """Set a world setting (setting, status). keys: world_immutable, nametags_visible"""
        self._conn.send("world.setting", setting, 1 if bool(status) else 0)

if __name__ == "__main__":
    mc = Minecraft()
    mc.postToChat("Hello, Minecraft!")
