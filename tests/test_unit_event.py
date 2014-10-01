import unittest
from minecraft.event import BlockEvent


class TestEvent(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInstantiation(self):
        evntType = 0
        pos = [14, 15, 16]
        face = 2
        entity = 1
        evnt = BlockEvent(evntType, pos[0], pos[1], pos[2], face, entity)
        self.assertEqual(evnt.type, evntType)
        self.assertEqual(evnt.pos.x, pos[0])
        self.assertEqual(evnt.pos.y, pos[1])
        self.assertEqual(evnt.pos.z, pos[2])
        self.assertEqual(evnt.face, face)
        self.assertEqual(evnt.entityId, entity)

    def testRepresentation(self):
        data = [0, 14, 15, 16, 1, 1]
        evnt = BlockEvent(data[0], data[1], data[2],
                          data[3], data[4], data[5])
        expected = "BlockEvent({}, {:2f}, {:2f}, {:2f}, {:d}, {:d})".format(
            data[0], data[1], data[2], data[3], data[4], data[5])
        rep = repr(evnt)
        self.assertTrue(rep, expected)

    def testStaticHit(self):
        x = 89
        y = -34
        z = 30
        evntType = 0
        face = 3
        entity = 1
        evnt = BlockEvent(BlockEvent.HIT, x, y, z, face, entity)
        self.assertEqual(evnt.type, evntType)
        self.assertEqual(evnt.pos.x, x)
        self.assertEqual(evnt.pos.y, y)
        self.assertEqual(evnt.pos.z, z)
        self.assertEqual(evnt.face, face)
        self.assertEqual(evnt.entityId, entity)
