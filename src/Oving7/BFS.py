from Graph import GraphNode, import_graph, Graph
from Queue import Queue


def bfs(graph: Graph, from_node: GraphNode):
    # Reset nodes
    for node in graph.nodes:
        node.dist = -1
        node.predecessor = None

    from_node.dist = 0

    queue = Queue()
    queue.enqueue(from_node)
    while not queue.empty():
        current_node = queue.dequeue()
        # print("Current node: {}".format(current_node.label))
        for neighbor in current_node.get_neighbors():
            # print("    Neighbor: {}".format(neighbor.label))
            if neighbor.dist < 0:
                neighbor.dist = current_node.dist + 1
                neighbor.predecessor = current_node
                queue.enqueue(neighbor)


"""
names = {}

print("Reading names file...")
with open("C:\L7Skandinavia-navn", "r", encoding="utf-8") as name_file:
    name_file.readline()  # Skip første linje med antall
    for raw_line in name_file:
        parts = raw_line.rstrip().split("\t")
        names[int(parts[0])] = parts[2][1:-1]
"""

if __name__ == "__main__":
    graph = import_graph("C:\L7g1")

    start_node: GraphNode = graph.nodes[5]
    print("Running BFS from node {}".format(start_node.label))
    bfs(graph, start_node)

    print("\nNode    Pred.   Dist.")
    for node in graph.nodes:
        predecessor = node.predecessor.label if node.predecessor is not None else " "
        print("   {}       {}       {}".format(node.label, predecessor, node.dist))
