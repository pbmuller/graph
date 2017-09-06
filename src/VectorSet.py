from src.Vector import Vector
from src.Node import Node


class VectorSet(list):
    """
    Params:
        parent_node: required
        vectors: iterable (not a string) collection of vector objects that the VectorSet will be initialized with.

    Initializes a vector set operates in much the same was a python set except it may only contain objects of the type Vector
    and all of the vectors must be related to the parent in some way, so the parent node of the set must be either the
    starting node or the finishing node of the vector.

    Exceptions:
        TypeError: vector param must be iterable
        TypeError: the members of the vector param must all be objects of type vector
        TypeError: parent_node param must be of type Node and not NULLNODE
    """
    def __init__(self, parent_node, vectors=[]):
        try:
            iter(vectors)
        except TypeError:
            raise TypeError('vectors param must be iterable')
        for vector in vectors:
            if not isinstance(vector, Vector):
                raise TypeError('the members of the vectors param must all be objects of type vector')
        if not isinstance(parent_node, Node) and parent_node is not Node.NULLNODE:
            raise TypeError('parent_node param must be of type Node and not NULLNODE')
        self.parent_node = parent_node
        super().__init__(vectors)

    """
    Params:
        vector

    Adds specified vector to vector set if the vector is not already in the vector set. If the vector is successful
    added, the add returns true. Otherwise, returns false.
    
    Exceptions:
        TypeError: the object that is being added must be of type Vector
    """
    def add(self, vector):
        if not isinstance(vector, Vector):
            raise TypeError('You may only add objects of type Vector to the vector set')
        if vector not in self:
            super().append(vector)
            return True
        else:
            return False

    """
    """
    def remove(self, vector):
        try:
            super().remove(vector)
            return True
        except ValueError:
            return False

    def __repr__(self):
        return self
