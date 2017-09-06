from src.Vector import Vector
from src.Node import Node


class VectorSet(list):
    """
    Params:
        parent_node: required
        vectors:
    """
    def __init__(self, parent_node, vectors=[]):
        try:
            iter(vectors)
        except TypeError:
            raise TypeError('vectors param must be iterable')
        for vector in vectors:
            if not isinstance(vector, Vector):
                raise TypeError('the members of the vectors param must all be ojects of type vector')
        if not isinstance(parent_node, Node) and parent_node is not Node.NULLNODE:
            raise TypeError('parent_node param must be of type Node and not the null Node')
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

    def __repr__(self):
        return self
