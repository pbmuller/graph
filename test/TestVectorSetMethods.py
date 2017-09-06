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


if __name__ == '__main__':
    unittest.main()