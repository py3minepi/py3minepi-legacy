import unittest
from minecraft.block import Block
from minecraft.block import blockType


class TestBlock(unittest.TestCase):

    def testRepresentation(self):
        # Test repr
        b = Block(2, 8)
        expectedString = "Block({:d}, {:d})".format(b.type, b.data)
        rep = repr(b)
        self.assertEqual(rep, expectedString)

    def testInstantiationAndWithDataFunction(self):
        blck = Block(12)
        self.assertEqual(blck.type, 12)
        self.assertEqual(blck.data, 0)
        blckWithData = Block(12, 4)
        self.assertEqual(blckWithData.type, 12)
        self.assertEqual(blckWithData.data, 4)
        otherBlckWithData = blck.withData(8)
        self.assertEqual(otherBlckWithData.type, 12)
        self.assertEqual(otherBlckWithData.data, 8)

    def testBackwardsCompatibility(self):
        blck = Block(12)
        self.assertEqual(blck.type, blck.id)

    def testComparison(self):
        b1 = Block(8, 3)
        bSame = Block(8, 3)
        bDiffId = Block(12, 3)
        bDiffData = Block(8, 7)
        bDiffIdAndData = Block(51, 7)

        self.assertTrue(b1 == b1)
        self.assertTrue(b1 == bSame)
        self.assertTrue(b1 != bDiffId)
        self.assertTrue(b1 != bDiffData)
        self.assertTrue(b1 != bDiffIdAndData)

        self.assertTrue(bDiffId > b1)
        self.assertTrue(bDiffData > b1)
        self.assertTrue(bDiffIdAndData > b1)

    def testIteration(self):
        idAndData = [35, 4]
        b = Block(idAndData[0], idAndData[1])
        for index, attr in enumerate(b):
            self.assertEqual(attr, idAndData[index])

    def testBlockConstants(self):
        self.assertEqual(blockType.AIR,  0)
        self.assertEqual(blockType.STONE,  1)
        self.assertEqual(blockType.GRASS,  2)
        self.assertEqual(blockType.DIRT,  3)
        self.assertEqual(blockType.COBBLESTONE, 4)
        self.assertEqual(blockType.WOOD_PLANKS,  5)
        self.assertEqual(blockType.SAPLING,  6)
        self.assertEqual(blockType.BEDROCK,  7)
        self.assertEqual(blockType.WATER_FLOWING,  8)
        self.assertEqual(blockType.WATER,  blockType.WATER_FLOWING)
        self.assertEqual(blockType.WATER_STATIONARY, 9)
        self.assertEqual(blockType.LAVA_FLOWING,  10)
        self.assertEqual(blockType.LAVA,  blockType.LAVA_FLOWING)
        self.assertEqual(blockType.LAVA_STATIONARY, 11)
        self.assertEqual(blockType.SAND,  12)
        self.assertEqual(blockType.GRAVEL,  13)
        self.assertEqual(blockType.GOLD_ORE,  14)
        self.assertEqual(blockType.IRON_ORE,  15)
        self.assertEqual(blockType.COAL_ORE,  16)
        self.assertEqual(blockType.WOOD,  17)
        self.assertEqual(blockType.LEAVES,  18)
        self.assertEqual(blockType.GLASS,  20)
        self.assertEqual(blockType.LAPIS_LAZULI_ORE, 21)
        self.assertEqual(blockType.LAPIS_LAZULI_BLOCK, 22)
        self.assertEqual(blockType.SANDSTONE,  24)
        self.assertEqual(blockType.BED,  26)
        self.assertEqual(blockType.COBWEB,  30)
        self.assertEqual(blockType.GRASS_TALL,  31)
        self.assertEqual(blockType.WOOL,  35)
        self.assertEqual(blockType.FLOWER_YELLOW,  37)
        self.assertEqual(blockType.FLOWER_CYAN,  38)
        self.assertEqual(blockType.MUSHROOM_BROWN,  39)
        self.assertEqual(blockType.MUSHROOM_RED,  40)
        self.assertEqual(blockType.GOLD_BLOCK,  41)
        self.assertEqual(blockType.IRON_BLOCK,  42)
        self.assertEqual(blockType.STONE_SLAB_DOUBLE, 43)
        self.assertEqual(blockType.STONE_SLAB,  44)
        self.assertEqual(blockType.BRICK_BLOCK,  45)
        self.assertEqual(blockType.TNT,  46)
        self.assertEqual(blockType.BOOKSHELF,  47)
        self.assertEqual(blockType.MOSS_STONE,  48)
        self.assertEqual(blockType.OBSIDIAN,  49)
        self.assertEqual(blockType.TORCH,  50)
        self.assertEqual(blockType.FIRE,  51)
        self.assertEqual(blockType.STAIRS_WOOD,  53)
        self.assertEqual(blockType.CHEST,  54)
        self.assertEqual(blockType.DIAMOND_ORE,  56)
        self.assertEqual(blockType.DIAMOND_BLOCK,  57)
        self.assertEqual(blockType.CRAFTING_TABLE,  58)
        self.assertEqual(blockType.FARMLAND,  60)
        self.assertEqual(blockType.FURNACE_INACTIVE, 61)
        self.assertEqual(blockType.FURNACE_ACTIVE,  62)
        self.assertEqual(blockType.DOOR_WOOD,  64)
        self.assertEqual(blockType.LADDER,  65)
        self.assertEqual(blockType.STAIRS_COBBLESTONE, 67)
        self.assertEqual(blockType.DOOR_IRON,  71)
        self.assertEqual(blockType.REDSTONE_ORE,  73)
        self.assertEqual(blockType.SNOW,  78)
        self.assertEqual(blockType.ICE,  79)
        self.assertEqual(blockType.SNOW_BLOCK,  80)
        self.assertEqual(blockType.CACTUS,  81)
        self.assertEqual(blockType.CLAY,  82)
        self.assertEqual(blockType.SUGAR_CANE,  83)
        self.assertEqual(blockType.FENCE,  85)
        self.assertEqual(blockType.GLOWSTONE_BLOCK, 89)
        self.assertEqual(blockType.BEDROCK_INVISIBLE, 95)
        self.assertEqual(blockType.STONE_BRICK,  98)
        self.assertEqual(blockType.GLASS_PANE,  102)
        self.assertEqual(blockType.MELON,  103)
        self.assertEqual(blockType.FENCE_GATE,  107)
        self.assertEqual(blockType.GLOWING_OBSIDIAN, 246)
        self.assertEqual(blockType.NETHER_REACTOR_CORE, 247)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBlock)
    unittest.TextTestRunner(verbosity=2).run(suite)
