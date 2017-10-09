from functools import total_ordering
import sys
from EdgeSort import quicksort


class CompactGraph:
    nodes = []
    edges = []


@total_ordering
class EdgeEntry:
    from_node = None
    to_node = None

    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node

    def __eq__(self, other):
        return self.from_node == other.from_node

    def __lt__(self, other):
        return self.from_node < other.from_node

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "{} -> {}".format(self.from_node, self.to_node)


def import_compact_graph(filename):
    graph = CompactGraph()
    edge_entries = []

    with open(filename, "r", encoding="utf-8") as graph_file:
        num_line = graph_file.readline().split()
        num_nodes, num_edges = int(num_line[0]), int(num_line[1])
        print("{} nodes, {} edges".format(num_nodes, num_edges))

        graph.nodes = [None] * num_nodes
        graph.edges = [None] * num_edges

        print("Reading edge entries...")
        for raw_line in graph_file:
            parts = raw_line.split()
            from_node = int(parts[0])
            to_node = int(parts[1])
            edge_entries.append(EdgeEntry(from_node, to_node))

    print("Memory usage of edge entries: {}".format(sys.getsizeof(edge_entries)))
    print("Sorting edge entries...")
    quicksort(edge_entries)

    print("Generating node and edge arrays...")
    for edge_entry in edge_entries:
        pass

    print("Done")

    return graph


if __name__ == "__main__":
    """
    a = EdgeEntry(0, 1)
    b = EdgeEntry(1, 2)
    c = EdgeEntry(2, 1)
    d = EdgeEntry(0, 2)
    arr = [a, b, c, d, EdgeEntry(-6,0), EdgeEntry(4,7), EdgeEntry(1,3)]

    assert a == d     # True
    assert not a > b  # False
    assert c > b      # True
    assert d <= a     # True
    """

    import_compact_graph("C:\L7Skandinavia")
