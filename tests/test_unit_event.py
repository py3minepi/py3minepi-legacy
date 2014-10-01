import unittest
from minecraft.event import BlockEvent


class TestEvent(unittest.TestCase):

    def testInstantiation(self):
        eventType = 0
        pos = [14, 15, 16]
        face = 2
        entity = 1
        event = BlockEvent(eventType, pos[0], pos[1], pos[2], face, entity)
        self.assertEqual(event.type, eventType)
        self.assertEqual(event.pos.x, pos[0])
        self.assertEqual(event.pos.y, pos[1])
        self.assertEqual(event.pos.z, pos[2])
        self.assertEqual(event.face, face)
        self.assertEqual(event.entityId, entity)

    def testRepresentation(self):
        data = [0, 14, 15, 16, 1, 1]
        event = BlockEvent(data[0], data[1], data[2],
                          data[3], data[4], data[5])
        expected = "BlockEvent({}, {:2f}, {:2f}, {:2f}, {:d}, {:d})".format(
            data[0], data[1], data[2], data[3], data[4], data[5])
        rep = repr(event)
        self.assertTrue(rep, expected)

    def testStaticHit(self):
        x = 89
        y = -34
        z = 30
        eventType = 0
        face = 3
        entity = 1
        event = BlockEvent(BlockEvent.HIT, x, y, z, face, entity)
        self.assertEqual(event.type, eventType)
        self.assertEqual(event.pos.x, x)
        self.assertEqual(event.pos.y, y)
        self.assertEqual(event.pos.z, z)
        self.assertEqual(event.face, face)
        self.assertEqual(event.entityId, entity)
