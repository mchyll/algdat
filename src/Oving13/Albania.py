import math
import time
from AStar import astar
from AStarGraph import import_astar_graph, import_names
from Dijkstra import dijkstra  # Dijkstra.py i mappen Oving8/


names = import_names("c:\\albania-interessepkt")
graph = import_astar_graph("C:\\albania-noder", "C:\\albania-kanter", names)

start_node = graph.nodes[36658]  # Korçë
end_node = graph.nodes[43011]    # Vlorë

print("Running Dijkstra from node {} to node {}".format(start_node.label, end_node.label))
start_time = time.time()
dijkstra(graph, start_node, end_node)
elapsed = time.time() - start_time
print("Done, time elapsed: {} s".format(elapsed))
print("Distance from {} to {}: {}".format(start_node.label, end_node.label, end_node.dist))

print("Running A* from node {} to node {}".format(start_node.label, end_node.label))
start_time = time.time()
astar(graph, start_node, end_node)
elapsed = time.time() - start_time
print("Done, time elapsed: {} s".format(elapsed))

if end_node.dist != math.inf:
    print("Distance from {} to {}: {}\n".format(start_node.label, end_node.label, end_node.dist))
    node = end_node
    while node is not None:
        print("{},{}".format(node.lat, node.long))
        node = node.predecessor
