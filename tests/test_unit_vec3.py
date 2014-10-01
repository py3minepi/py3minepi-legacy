import unittest
from minecraft.vec3 import Vec3


class TestVec3(unittest.TestCase):
    """ Test the functions of the Vec3 class """

    def test_instantiation(self):
        expect_x = -1.0
        expect_y = 4.0
        expect_z = 6.0
        v = Vec3(expect_x, expect_y, expect_z)
        self.assertEqual(
            v.x, expect_x,
            "Expect {:f} to be equal to {:f} but wasn't ".format(v.x, expect_x)
            )
        self.assertEqual(
            v.y, expect_y,
            "Expect {:f} to be equal to {:f} but wasn't ".format(v.y, expect_y)
            )
        self.assertEqual(
            v.z, expect_z,
            "Expect {:f} to be equal to {:f} but wasn't ".format(v.z, expect_z)
            )

    def test_representation(self):
        # Test repr
        v1 = Vec3(2, -3, 8)
        expected_string = "Vec3({},{},{})".format(v1.x, v1.y, v1.z)
        rep = repr(v1)
        self.assertEqual(rep, expected_string)

    def test_iteration(self):
        coords = [1, 9, 6]
        v = Vec3(coords[0], coords[1], coords[2])
        for index, pos in enumerate(v):
            self.assertEqual(pos, coords[index])

    def test_equality(self):
        v1 = Vec3(2, -3, 8)
        v_same = Vec3(2, -3, 8)
        v_diff = Vec3(22, 63, 88)
        v_x_larger = Vec3(5, -3, 8)
        v_x_smaller = Vec3(0, -3, 8)
        v_y_larger = Vec3(2, 9, 8)
        v_y_smaller = Vec3(2, -10, 8)
        v_z_larger = Vec3(2, -3, 12)
        v_z_smaller = Vec3(2, -3, 4)

        self.assertTrue(
            v1 == v_same,
            "Expected {} to be equal to {} but wasn't ".format(v1, v_same)
            )
        self.assertFalse(
            v1 == v_diff,
            "Expected {} to be not equal to {} but wasn't ".format(v1, v_diff)
            )
        self.assertTrue(
            v1 != v_diff,
            "Expected {} to be not equal to {} but wasn't ".format(v1, v_diff)
            )
        otherVectors = [v_x_larger, v_y_larger, v_z_larger,
                        v_x_smaller, v_y_smaller, v_z_smaller]

        for other in otherVectors:
            self.assertTrue(v1 != other,
            "Expected {} to be not equal to {} but wasn't ".format(v1, other))

        for other in otherVectors:
            self.assertFalse(v1 == other,
            "Expected {} to be not equal to {} but wasn't ".format(v1, other))


    def test_cloning(self):
        v = Vec3(2, -3, 8)
        v_clone = v.clone()
        self.assertTrue(v == v_clone)
        v.x += 1
        self.assertTrue(v != v_clone)

    def test_negation(self):
        v1 = Vec3(2, -3, 8)
        v_inverse = -v1
        self.assertEqual(v1.x, -v_inverse.x)
        self.assertEqual(v1.y, -v_inverse.y)
        self.assertEqual(v1.z, -v_inverse.z)

    def test_addition(self):
        a = Vec3(10, -3, 4)
        b = Vec3(-7, 1, 2)
        c = a + b
        totV = Vec3(3, -2, 6)
        self.assertEqual(c, totV)
        d = c - b
        self.assertEqual(d, a)

    def test_subtraction(self):
        a = Vec3(10, -3, 4)
        b = Vec3(5, 3, 5)
        self.assertEqual((a - a), Vec3(0, 0, 0))
        self.assertEqual((a + (-a)), Vec3(0, 0, 0))
        self.assertEqual((a - b), Vec3(5, -6, -1))

    def test_multiplication(self):
        a = Vec3(2, -3, 8)
        self.assertEqual((a + a), (a * 2))
        k = 4
        a *= k
        self.assertEqual(a, Vec3(2 * k, -3 * k, 8 * k))

    def test_length(self):
        v = Vec3(2, -3, 8)
        l = v.length()
        ls = ((2 * 2) + (-3 * -3) + (8 * 8))
        self.assertEqual(l, (ls ** 0.5))

    def test_length_sqr(self):
        v = Vec3(2, -3, 8)
        ls = v.lengthSqr()
        self.assertEqual(ls, ((2 * 2) + (-3 * -3) + (8 * 8)))

    def test_distance_to(self):
        coords_one = [2, -3, 8]
        coords_two = [-4, 5, 12]
        v1 = Vec3(coords_one[0], coords_one[1], coords_one[2])
        v2 = Vec3(coords_two[0], coords_two[1], coords_two[2])
        expect_dist = (((coords_two[0] - coords_one[0]) ** 2) +
                      ((coords_two[1] - coords_one[1]) ** 2) +
                      ((coords_two[2] - coords_one[2]) ** 2)) ** 0.5
        dist = v1.distanceTo(v2)
        self.assertEqual(dist, expect_dist)

    def test_iround(self):
        v = Vec3(2.3, -3.7, 8.8)
        v.iround()
        expect_vec = Vec3(2, -3, 9)
        self.assertEqual(v, expect_vec)

    def test_ifloor(self):
        v = Vec3(2.3, -3.7, 8.8)
        v.ifloor()
        expect_vec = Vec3(2, -3, 8)
        self.assertEqual(v, expect_vec)

    def test_rotate_left(self):
        v = Vec3(2, -3, 8)
        v.rotateLeft()
        expect_vec = Vec3(8, -3, -2)
        self.assertEqual(v, expect_vec)

    def test_rotate_right(self):
        v = Vec3(2, -3, 8)
        v.rotateRight()
        expect_vec = Vec3(-8, -3, 2)
        self.assertEqual(v, expect_vec)
