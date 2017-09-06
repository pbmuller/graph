from src.Vector import Vector


class Node:
    __special_status = ['none', 'sink', 'star']
    __node_ids = set()
    NULLNODE = None

    def __init__(self, node_id, neighbors=set()):
        if node_id not in Node.__node_ids:
            self.node_id = node_id
            Node.__node_ids.add(self.node_id)
        else:
            raise ValueError("Can't repeat node ids")
        self.vectors = self.__make_path(neighbors)
        self.__init_null_node()

    def __make_path(self, neighbors):
        vectors_to_neighbors = set()
        for neighbor in neighbors:
            vectors_to_neighbors.add(Vector.make_vector(self, neighbor, 1))
        return vectors_to_neighbors

    def __repr__(self):
        rep = 'node_id = {}\n'.format(self.node_id)
        rep += 'vectors\n'
        for vector in self.vectors:
            rep += '\t{}\n'.format(vector)
        return rep

    def add_neighbor(self, neighbor_node):
        if self == Node.NULLNODE:
            raise ValueError('You can node add neighbors to the NULLNODE')
        if not isinstance(neighbor_node, Node):
            raise TypeError("neighbor_node must be of type Node")
        # if neighbor_node in self.vectors

    def __init_null_node(self):
        if Node.NULLNODE is not None:
            self.__init__(None)