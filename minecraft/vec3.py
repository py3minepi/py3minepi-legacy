import math


class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, rhs):
        c = self.clone()
        c += rhs
        return c

    def __iadd__(self, rhs):
        self.x += rhs.x
        self.y += rhs.y
        self.z += rhs.z
        return self

    def length(self):
        return self.lengthSqr() ** .5

    def lengthSqr(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def __mul__(self, k):
        c = self.clone()
        c *= k
        return c

    def __imul__(self, k):
        self.x *= k
        self.y *= k
        self.z *= k
        return self

    def clone(self):
        return Vec3(self.x, self.y, self.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __sub__(self, rhs):
        return self.__add__(-rhs)

    def __isub__(self, rhs):
        return self.__iadd__(-rhs)

    def __repr__(self):
        return 'Vec3({},{},{})'.format(self.x, self.y, self.z)

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def _map(self, func):
        self.x = func(self.x)
        self.y = func(self.y)
        self.z = func(self.z)

    def __eq__(self, other):
        return all([self.x == other.x, self.y == other.y, self.z == other.z])

    def __ne__(self, other):
        return not (self == other)

    def iround(self):
        self._map(lambda v: int(v + 0.5))

    def ifloor(self):
        self._map(int)

    def rotateLeft(self):
        self.x, self.z = self.z, -self.x

    def rotateRight(self):
        self.x, self.z = -self.z, self.x

    def distanceTo(self, other):
        x_dist = other.x - self.x
        y_dist = other.y - self.y
        z_dist = other.z - self.z
        return math.sqrt(x_dist ** 2 + y_dist ** 2 + z_dist ** 2)
