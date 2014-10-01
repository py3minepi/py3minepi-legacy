import unittest
from minecraft.vec3 import Vec3


class TestVec3(unittest.TestCase):
    """ Test the functions of the Vec3 class """

    def testInstantiation(self):
        expectX = -1.0
        expectY = 4.0
        expectZ = 6.0
        v = Vec3(expectX, expectY, expectZ)
        self.assertEqual(
            v.x, expectX,
            "Expect {:f} to be equal to {:f} but wasn't ".format(v.x, expectX)
            )
        self.assertEqual(
            v.y, expectY,
            "Expect {:f} to be equal to {:f} but wasn't ".format(v.y, expectY)
            )
        self.assertEqual(
            v.z, expectZ,
            "Expect {:f} to be equal to {:f} but wasn't ".format(v.z, expectZ)
            )

    def testRepresentation(self):
        # Test repr
        v1 = Vec3(2, -3, 8)
        expectedString = "Vec3({},{},{})".format(v1.x, v1.y, v1.z)
        rep = repr(v1)
        self.assertEqual(rep, expectedString)

    def testIteration(self):
        coords = [1, 9, 6]
        v = Vec3(coords[0], coords[1], coords[2])
        for index, pos in enumerate(v):
            self.assertEqual(pos, coords[index])

    def testComparison(self):
        v1 = Vec3(2, -3, 8)
        vSame = Vec3(2, -3, 8)
        vDiff = Vec3(22, 63, 88)
        vXlarger = Vec3(5, -3, 8)
        vXsmaller = Vec3(0, -3, 8)
        vYlarger = Vec3(2, 9, 8)
        vYsmaller = Vec3(2, -10, 8)
        vZlarger = Vec3(2, -3, 12)
        vZsmaller = Vec3(2, -3, 4)

        self.assertTrue(
            v1 == vSame,
            "Expected {} to be equal to {} but wasn't ".format(v1, vSame)
            )
        self.assertFalse(
            v1 == vDiff,
            "Expected {} to be not equal to {} but wasn't ".format(v1, vDiff)
            )
        self.assertTrue(
            v1 != vDiff,
            "Expected {} to be not equal to {} but wasn't " .format(v1, vDiff)
            )

        self.assertTrue(
            v1 < vXlarger,
            "Expected {} to be less than {} but wasn't " .format(v1, vXlarger)
            )
        self.assertTrue(
            v1 < vYlarger,
            "Expected {} to be less than {} but wasn't " .format(v1, vYlarger)
            )
        self.assertTrue(
            v1 < vZlarger,
            "Expected {} to be less than {} but wasn't " .format(v1, vZlarger)
            )

        self.assertTrue(
            v1 > vXsmaller,
            "Expected {} to be more than {} but wasn't " .format(v1, vXsmaller)
            )
        self.assertTrue(
            v1 > vYsmaller,
            "Expected {} to be more than {} but wasn't " .format(v1, vXsmaller)
            )
        self.assertTrue(
            v1 > vZsmaller,
            "Expected {} to be more than {} but wasn't " .format(v1, vXsmaller)
            )

    def testCloning(self):
        v = Vec3(2, -3, 8)
        vClone = v.clone()
        self.assertTrue(v == vClone)
        v.x += 1
        self.assertTrue(v != vClone)

    def testNegation(self):
        v1 = Vec3(2, -3, 8)
        vInverse = -v1
        self.assertEqual(v1.x, -vInverse.x)
        self.assertEqual(v1.y, -vInverse.y)
        self.assertEqual(v1.z, -vInverse.z)

    def testAddition(self):
        a = Vec3(10, -3, 4)
        b = Vec3(-7, 1, 2)
        c = a + b
        totV = Vec3(3, -2, 6)
        self.assertEqual(c, totV)
        d = c - b
        self.assertEqual(d, a)

    def testSubtraction(self):
        a = Vec3(10, -3, 4)
        b = Vec3(5, 3, 5)
        self.assertEqual((a - a), Vec3(0, 0, 0))
        self.assertEqual((a + (-a)), Vec3(0, 0, 0))
        self.assertEqual((a - b), Vec3(5, -6, -1))

    def testMultiplication(self):
        a = Vec3(2, -3, 8)
        self.assertEqual((a + a), (a * 2))
        k = 4
        a *= k
        self.assertEqual(a, Vec3(2 * k, -3 * k, 8 * k))

    def testLength(self):
        v = Vec3(2, -3, 8)
        l = v.length
        ls = ((2 * 2) + (-3 * -3) + (8 * 8))
        self.assertEqual(l, (ls ** 0.5))

    def testLengthSqr(self):
        v = Vec3(2, -3, 8)
        ls = v.lengthSqr
        self.assertEqual(ls, ((2 * 2) + (-3 * -3) + (8 * 8)))

    def testDistance(self):
        coords_one = [2, -3, 8]
        coords_two = [-4, 5, 12]
        v1 = Vec3(coords_one[0], coords_one[1], coords_one[2])
        v2 = Vec3(coords_two[0], coords_two[1], coords_two[2])
        expectDist = (((coords_two[0] - coords_one[0]) ** 2) +
                      ((coords_two[1] - coords_one[1]) ** 2) +
                      ((coords_two[2] - coords_one[2]) ** 2)) ** 0.5
        dist = v1.distanceTo(v2)
        self.assertEqual(dist, expectDist)

    def testIround(self):
        v = Vec3(2.3, -3.7, 8.8)
        v.iround()
        expectVec = Vec3(2, -3, 9)
        self.assertEqual(v, expectVec)

    def testIfloor(self):
        v = Vec3(2.3, -3.7, 8.8)
        v.ifloor()
        expectVec = Vec3(2, -3, 8)
        self.assertEqual(v, expectVec)

    def testRotateLeft(self):
        v = Vec3(2, -3, 8)
        v.rotateLeft()
        expectVec = Vec3(8, -3, -2)
        self.assertEqual(v, expectVec)

    def testRotateRight(self):
        v = Vec3(2, -3, 8)
        v.rotateRight()
        expectVec = Vec3(-8, -3, 2)
        self.assertEqual(v, expectVec)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestVec3)
    unittest.TextTestRunner(verbosity=2).run(suite)
