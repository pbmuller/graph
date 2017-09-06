class Vector:
    __valid_kinds = {'one-way', 'two-way'}

    def __init__(self, endpoint_nodes, weight=0, kind='two-way'):
        self.endpoints_nodes = endpoint_nodes
        self.weight = weight
        if kind not in Vector.__valid_kinds:
            raise ValueError("Invalid kind for Vector")
        self.kind = kind

    def __repr__(self):
        return 'weight = {}, {}'.format(
            self.weight,
            'ONE-Way: from node {} to node {}'.format(
                self.endpoints_nodes[0],
                self.endpoints_nodes[1]
            ) if self.kind == 'one-way' else
            'TWO-Way: node {} and node {}'.format(
                self.endpoints_nodes[0],
                self.endpoints_nodes[1]
            )
        )

    def __eq__(self, other):
        return (self.endpoints_nodes == other.endpoints_nodes) and (self.weight == other.weight)

    def __ne__(self, other):
        return self.endpoints_nodes != other.endpoints_nodes or self.weight != other.weight

    @classmethod
    def make_vector(cls, node1, node2, weight, kind='two-way'):
        return cls((node1, node2), weight, kind)