import sys

from Graph import Graph, GraphNode
from Queue import Queue


def bfs(graph, from_node):
    for node in graph.nodes:
        node.dist = -1

    from_node.dist = 0
    queue = Queue()
    queue.enqueue(from_node)
    while not queue.empty():
        node = queue.dequeue()
        for neighbor in node.get_neighbors():
            if neighbor.dist < 0:
                neighbor.dist = node.dist + 1
                neighbor.predecessor = node
                queue.enqueue(neighbor)


names = {}

"""
print("Reading names file...")
with open("C:\L7Skandinavia-navn", "r", encoding="utf-8") as name_file:
    name_file.readline()  # Skip første linje med antall
    for raw_line in name_file:
        parts = raw_line.rstrip().split("\t")
        names[int(parts[0])] = parts[2][1:-1]
"""


graph = Graph()
with open("C:\L7g3", "r", encoding="utf-8") as graph_file:
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

start_node = graph.nodes[0]
print("Running BFS from node {}".format(start_node.label))
bfs(graph, start_node)

node = graph.nodes[10]
while node != start_node:
    print("{} -> ".format(node.label), end='')
    node = node.predecessor
