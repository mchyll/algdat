import math


class AStarGraph:
    nodes = []


class AStarGraphEdge:
    to_node = None
    weight = 0

    def __init__(self, to_node, weight):
        self.to_node = to_node
        self.weight = weight


class AStarGraphNode:
    label = None
    edges = []

    lat = 0
    long = 0
    est_dist = -1

    dist = math.inf
    prio = math.inf
    predecessor = None
    heap_pos = -1

    def __init__(self, label=None):
        self.label = label
        self.edges = []

    def add_edge_to(self, other_node, weight):
        self.edges.append(AStarGraphEdge(other_node, weight))

    def get_neighbors(self):
        for edge in self.edges:
            yield edge.to


def import_astar_graph(nodes_filename, edges_filename, names=None):
    if names is None:
        names = {}

    graph = AStarGraph()
    with open(nodes_filename, "r", encoding="utf-8") as nodes_file, open(edges_filename, "r", encoding="utf-8") as edges_file:
        num_nodes = int(nodes_file.readline().strip())
        num_edges = int(edges_file.readline().strip())
        print("{} nodes, {} edges".format(num_nodes, num_edges))
        print("Generating node objects...")
        graph.nodes = [None] * num_nodes

        for raw_line in nodes_file:
            parts = raw_line.split()
            node_num = int(parts[0])
            name = names[node_num] if node_num in names else node_num
            node = AStarGraphNode(name)
            node.lat = float(parts[1])
            node.long = float(parts[2])
            graph.nodes[node_num] = node

        print("Reading edge entries...")
        for raw_line in edges_file:
            parts = raw_line.split()
            from_node = int(parts[0])
            to_node = int(parts[1])
            weight = int(parts[2])
            graph.nodes[from_node].add_edge_to(graph.nodes[to_node], weight)

    print("Graph generated")
    return graph


def import_names(names_filename):
    names = {}
    print("Reading names file...")
    with open(names_filename, "r", encoding="utf-8") as name_file:
        name_file.readline()  # Skip første linje med antall
        for raw_line in name_file:
            parts = raw_line.rstrip().split()
            names[int(parts[0])] = parts[2][1:-1]

    return names
