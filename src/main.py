from src.Node import Node


def main():
    node_set = set()
    for i in range(2):
        node_set.add(Node(i))
    main_node = Node(2, node_set)
    print(main_node)

if __name__ == '__main__':
    main()