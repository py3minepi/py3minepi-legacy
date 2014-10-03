class position(tuple):
    '''An absolute integer position in Minecraft space.'''

    def __new__(cls, x, y, z):
        return tuple.__new__(cls, (x, y, z))

    @property
    def x(self):
        '''How far to the left.'''
        return self[0]

    @property
    def y(self):
        '''How far up.'''
        return self[1]

    @property
    def z(self):
        '''How far forward.'''
        return self[2]


def _incl_range(start, end):
    """
    Inclusive range between start and end.

    Start at start, finishes at end, and includes the end points.
    """
    if start <= end:
        return range(start, end + 1, 1)
    else:
        return range(start, end - 1, -1)


def region(start, end):
    """
    Yield all positions between start and end, including end points.

    The x value changes in the outermost loop, and then y and z.
    """
    for x in _incl_range(start.x, end.x):
        for y in _incl_range(start.y, end.y):
            for z in _incl_range(start.z, end.z):
                yield position(x, y, z)

# TODO: Allow pos in Region(start, end) ?

position(1, 2, 3)
assert position(1, 2, 3).x == 1
assert position(1, 2, 3).y == 2
assert position(1, 2, 3).z == 3

assert list(_incl_range(0, 0)) == [0]
assert list(_incl_range(0, 1)) == [0, 1]
assert list(_incl_range(1, 0)) == [1, 0]
assert list(_incl_range(0, 4)) == [0, 1, 2, 3, 4]
assert list(_incl_range(4, 0)) == [4, 3, 2, 1, 0]


def testit(start, end):
    return list(region(position(*start), position(*end)))


assert testit((1, 2, 3), (2, 3, 4)) == [
        (1, 2, 3), (1, 2, 4),
        (1, 3, 3), (1, 3, 4),
        (2, 2, 3), (2, 2, 4),
        (2, 3, 3), (2, 3, 4),
]
