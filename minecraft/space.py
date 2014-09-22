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
        '''The far forward.'''
        return self[2]


def _incl_range(start, end):
    '''Inclusive range between start and end.'''

    sgn = 1 if start <= end else -1
    if start <= end:
        return range(start, end + 1, 1)
    else:
        return range(start, end - 1, -1)

def region(start, end):
    '''Yield all positions in rectangular region start to end.'''
    for x in _incl_range(start.x, end.x):
        for y in _incl_range(start.y, end.y):
            for z in _incl_range(start.z, end.z):
                yield position(x, y, z)


position(1, 2, 3)
position(1, 2, 3).x == 1

def testit(start, end):
    return list(region(position(*start), position(*end)))


list(_incl_range(0, 0)) == [0]
list(_incl_range(0, 1)) == [0, 1]
list(_incl_range(1, 0)) == [1, 0]
list(_incl_range(0, 4)) == [0, 1, 2, 3, 4]
list(_incl_range(4, 0)) == [4, 3, 2, 1, 0]

for pos in testit((1, 2, 3), (4, 5 ,6)):
    print(pos)
