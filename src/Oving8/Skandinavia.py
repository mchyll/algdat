import math
import time
from Dijkstra import dijkstra
from WeightedGraph import import_weighted_graph

names = {}

print("Reading names file...")
with open("C:\L7Skandinavia-navn", "r", encoding="utf-8") as name_file:
    name_file.readline()  # Skip første linje med antall
    for raw_line in name_file:
        parts = raw_line.rstrip().split()
        names[int(parts[0])] = parts[2][1:-1]

graph = import_weighted_graph("C:\\vgSkandinavia", names)
start_node = graph.nodes[37774]  # 37774 er Kalvskinnet
end_node = graph.nodes[18058]  # 18058 er Moholt
print("Running Dijkstra from node {} to node {}".format(start_node.label, end_node.label))
start_time = time.time()
dijkstra(graph, start_node, end_node)
elapsed = time.time() - start_time
print("Done, time elapsed: {} s".format(elapsed))

if end_node.dist != math.inf:
    print("Distance from {} to {}: {}".format(start_node.label, end_node.label, end_node.dist))
    node = end_node
    while node is not None:
        print(node.label)
        node = node.predecessor
