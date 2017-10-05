from LinkedList import UnorderedLinkedList


class Graph:
    nodes = []


class GraphNode:
    label = None
    edges = None

    def __init__(self, label=None):
        self.label = label
        self.edges = UnorderedLinkedList()

    def add_edge_to(self, other_node):
        self.edges.add(other_node)


def import_graph(filename):
    graph = Graph()
    with open(filename, "r", encoding="utf-8") as graph_file:
        num_line = graph_file.readline().split()
        num_nodes, num_edges = int(num_line[0]), int(num_line[1])
        graph.nodes = [None] * num_nodes

        for i in range(num_nodes):
            node = GraphNode()
            graph.nodes[i] = node

        for raw_line in graph_file:
            parts = raw_line.split()
            from_node = int(parts[0])
            to_node = int(parts[1])
            graph.nodes[from_node].edges.add(graph.nodes[to_node])

    return graph
