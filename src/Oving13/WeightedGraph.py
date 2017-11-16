class WeightedGraph:
    nodes = []


class WeightedGraphEdge:
    to_node = None
    weight = 0

    def __init__(self, to_node, weight):
        self.to_node = to_node
        self.weight = weight


class WeightedGraphNode:
    label = None
    edges = []

    # Variables used in Dijkstra and MinHeap
    dist = -1
    predecessor = None
    heap_pos = -1

    def __init__(self, label=None):
        self.label = label
        self.edges = []

    def add_edge_to(self, other_node, weight):
        self.edges.append(WeightedGraphEdge(other_node, weight))

    def get_neighbors(self):
        for edge in self.edges:
            yield edge.to


def import_weighted_graph(filename, names=None):
    if names is None:
        names = {}

    graph = WeightedGraph()
    with open(filename, "r", encoding="utf-8") as graph_file:
        num_line = graph_file.readline().split()
        num_nodes, num_edges = int(num_line[0]), int(num_line[1])
        print("{} nodes, {} edges".format(num_nodes, num_edges))

        graph.nodes = [None] * num_nodes

        print("Generating node objects...")
        for i in range(num_nodes):
            name = names[i] if i in names else i
            node = WeightedGraphNode(name)
            graph.nodes[i] = node

        print("Reading edge entries...")
        for raw_line in graph_file:
            parts = raw_line.split()
            from_node = int(parts[0])
            to_node = int(parts[1])
            weight = int(parts[2])
            graph.nodes[from_node].add_edge_to(graph.nodes[to_node], weight)

    print("Graph generated")
    return graph
