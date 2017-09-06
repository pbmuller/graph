from src.VectorSet import VectorSet
from src.Vector import Vector
from src.Node import Node
import unittest


class TestVectorSetMethods(unittest.TestCase):
    # define useful testing nodes
    parent_node = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    # define useful testing vectors
    vP1 = Vector((parent_node, n1))
    vP2 = Vector((parent_node, n2))
    v12 = Vector((n1, n2))

    def test_len_0(self):
        vs = VectorSet(self.parent_node)
        self.assertEqual(len(vs), 0)

    def test_add(self):
        vs = VectorSet(self.parent_node)
        try:
            vs.add(self.vP1)
        except ValueError as ve:
            self.fail(ve.args)

    def test_add_repeat_vector(self):
        vs = VectorSet(self.parent_node)
        vs.add(self.vP1)
        self.assertEqual(vs.add(self.vP1), False)

    def test_len_same_after_failed_add(self):
        vs = VectorSet(self.parent_node)
        vs.add(self.vP1)
        length = len(vs)
        vs.add(self.vP1)
        self.assertEqual(len(vs), length)

    def test_remove_succeed(self):
        vs = VectorSet(self.parent_node)
        vs.add(self.vP1)
        self.assertEqual(vs.remove(self.vP1), True)

    def test_remove_failure(self):
        vs = VectorSet(self.parent_node)
        self.assertEqual(vs.remove(self.vP1), False)

    def test_in_true(self):
        vs = VectorSet(self.parent_node)
        vs.add(self.vP1)
        self.assertEqual(self.vP1 in vs, True)

    def test_in_false(self):
        vs = VectorSet(self.parent_node)
        self.assertEqual(self.vP1 in vs, False)


if __name__ == '__main__':
    unittest.main()