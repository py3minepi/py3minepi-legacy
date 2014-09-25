from .vec3 import Vec3


class BlockEvent:
    """An Event related to blocks (e.g. placed, removed, hit)"""
    HIT = 0

    def __init__(self, type, x, y, z, face, entityId):
        self.type = type
        self.pos = Vec3(x, y, z)
        self.face = face
        self.entityId = entityId

    def __repr__(self):
        # TODO: untangle .HIT and .Hit
        sType = {
            BlockEvent.HIT: "BlockEvent.HIT"
        }.get(self.type, "???")

        args = (
            sType,
            self.pos.x,
            self.pos.y,
            self.pos.z,
            self.face,
            self.entityId
        )
        return 'BlockEvent({}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {})'.format(*args)

    @staticmethod
    def Hit(x, y, z, face, entityId):
        return BlockEvent(BlockEvent.HIT, x, y, z, face, entityId)
