from LinkedList import UnorderedLinkedList


class Graph:
    nodes = []


class GraphNode:
    label = None
    edges = None

    # Variables used in BFS and topological sort
    dist = -1
    predecessor = None
    found = False
    next_node = None

    def __init__(self, label=None):
        self.label = label
        self.edges = UnorderedLinkedList()

    def add_edge_to(self, other_node):
        self.edges.add(other_node)

    def get_neighbors(self):
        neighbor = self.edges.head
        while neighbor is not None:
            yield neighbor.value
            neighbor = neighbor.next


def import_graph(filename, names=None):
    if names is None:
        names = {}

    graph = Graph()
    with open(filename, "r", encoding="utf-8") as graph_file:
        num_line = graph_file.readline().split()
        num_nodes, num_edges = int(num_line[0]), int(num_line[1])
        print("{} nodes, {} edges".format(num_nodes, num_edges))

        graph.nodes = [None] * num_nodes

        print("Generating node objects...")
        for i in range(num_nodes):
            name = names[i] if i in names else i
            node = GraphNode(name)
            graph.nodes[i] = node

        print("Reading edge entries...")
        for raw_line in graph_file:
            parts = raw_line.split()
            from_node = int(parts[0])
            to_node = int(parts[1])
            graph.nodes[from_node].edges.add(graph.nodes[to_node])

    print("Graph generated")
    return graph
