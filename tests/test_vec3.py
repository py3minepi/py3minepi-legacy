from minecraft.vec3 import Vec3


def test_vec3():
    """
    Vec3 tests

    Note: These are not complete (yet)
    """
    # 1.1 Test initialization
    vector3 = Vec3(1, -2, 3)
    assert vector3.x == 1
    assert vector3.y == -2
    assert vector3.z == 3

    assert vector3.x != -1
    assert vector3.y != +2
    assert vector3.z != -3

    # 2.1 Test cloning and equality
    clone = vector3.clone()
    assert vector3 == clone
    vector3.x += 1
    assert vector3 != clone

    # 3.1 Arithmetic
    a = Vec3(10, -3, 4)
    b = Vec3(-7, 1, 2)
    c = a + b
    assert c - a == b
    assert c - b == a
    assert a + a == a * 2

    assert a - a == Vec3(0,0,0)
    assert a + (-a) == Vec3(0,0,0)

    # Test repr
    e = eval(repr(vector3))
    assert e == vector3
