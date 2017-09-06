import unittest
from src.Vector import Vector
from src.Node import Node


class TestVectorMethods(unittest.TestCase):
    n1 = Node(0)
    n2 = Node(1)

    def test_constructor(self):
        vector = Vector((self.n1, self.n2), 0)
        self.assertEqual(vector.endpoints_nodes, (self.n1, self.n2), "failed constructor node set")
        self.assertEqual(vector.weight, 0, "failed constructor weight")

    def test_equal(self):
        v1 = Vector((self.n1, self.n2), 0)
        v2 = Vector((self.n1, self.n2), 0)
        self.assertEqual(v1, v2, "failed equality")

    def test_not_equal_weight(self):
        v1 = Vector((self.n1, self.n2), 0)
        v2 = Vector((self.n1, self.n2), 4)
        self.assertNotEqual(v1, v2, "failed weight not equal")

    def test_not_equal_direction(self):
        v1 = Vector((self.n1, self.n2), 0)
        v2 = Vector((self.n2, self.n1), 0)
        self.assertNotEqual(v1, v2, "failed direction not equal")

    def test_make_vector(self):
        v1 = Vector.make_vector(self.n1, self.n2, 0)
        v2 = Vector((self.n1, self.n2), 0)
        self.assertEqual(v1, v2)

if __name__ == '__main__':
    unittest.main()
