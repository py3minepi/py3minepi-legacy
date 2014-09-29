import sys
if sys.version_info < (3, 4):
    from flufl.enum import Enum
else:
    from enum import Enum


class Block:
    """
    Minecraft PI block description. Can be sent to Minecraft.setBlock/s
    block.type = the blockID of a block (It's meterial)
    block.data = A unknown member that does something
    The default type for blocks is dirt
    """

    def __init__(self, type=3, data=0):
        self.type = type
        self.data = data

    def __cmp__(self, rhs):
        return hash(self) - hash(rhs)

    def __hash__(self):
        return (self.id << 8) + self.data

    #TODO: This looks wierd, does it have any use?
    def __iter__(self):
        """Allows a Block to be sent whenever id [and data] is needed"""
        return iter((self.id, self.data))
        
    def __repr__(self):
        return 'Block({}, {:.2f})'.format(self.id, self.data)

    #TODO: find out if this has any use
    def withData(self, data):
        return Block(self.id, data)


class blockType(Enum):
    AIR = 0
    STONE = 1
    GRASS = 2
    DIRT = 3
    COBBLESTONE = 4
    WOOD_PLANKS = 5
    SAPLING = 6
    BEDROCK = 7
    WATER_FLOWING = 8
    WATER = WATER_FLOWING
    WATER_STATIONARY = 9
    LAVA_FLOWING = 10
    LAVA = LAVA_FLOWING
    LAVA_STATIONARY = 11
    SAND = 12
    GRAVEL = 13
    GOLD_ORE = 14
    IRON_ORE = 15
    COAL_ORE = 16
    WOOD = 17
    LEAVES = 18
    GLASS = 20
    LAPIS_LAZULI_ORE = 21
    LAPIS_LAZULI_BLOCK = 22
    SANDSTONE = 24
    BED = 26
    COBWEB = 30
    GRASS_TALL = 31
    WOOL = 35
    FLOWER_YELLOW = 37
    FLOWER_CYAN = 38
    MUSHROOM_BROWN = 39
    MUSHROOM_RED = 40
    GOLD_BLOCK = 41
    IRON_BLOCK = 42
    STONE_SLAB_DOUBLE = 43
    STONE_SLAB = 44
    BRICK_BLOCK = 45
    TNT = 46
    BOOKSHELF = 47
    MOSS_STONE = 48
    OBSIDIAN = 49
    TORCH = 50
    FIRE = 51
    STAIRS_WOOD = 53
    CHEST = 54
    DIAMOND_ORE = 56
    DIAMOND_BLOCK = 57
    CRAFTING_TABLE = 58
    FARMLAND = 60
    FURNACE_INACTIVE = 61
    FURNACE_ACTIVE = 62
    DOOR_WOOD = 64
    LADDER = 65
    STAIRS_COBBLESTONE = 67
    DOOR_IRON = 71
    REDSTONE_ORE = 73
    SNOW = 78
    ICE = 79
    SNOW_BLOCK = 80
    CACTUS = 81
    CLAY = 82
    SUGAR_CANE = 83
    FENCE = 85
    GLOWSTONE_BLOCK = 89
    BEDROCK_INVISIBLE = 95
    STONE_BRICK = 98
    GLASS_PANE = 102
    MELON = 103
    FENCE_GATE = 107
    GLOWING_OBSIDIAN = 246
    NETHER_REACTOR_CORE = 247

