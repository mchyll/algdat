import math
import time
from AStar import astar
from AStarGraph import import_astar_graph, import_names
from Dijkstra import dijkstra  # Dijkstra.py i mappen Oving8/


def test_astar_dijkstra(graph, start_node, end_node, list_path=False):
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
    print("Distance from {} to {}: {}\n".format(start_node.label, end_node.label, end_node.dist))

    if list_path and end_node.dist != math.inf:
        node = end_node
        while node is not None:
            print("{},{}".format(node.lat, node.long))
            node = node.predecessor


if __name__ == "__main__":
    albania_names = import_names("c:\\albania-interessepkt")
    albania_graph = import_astar_graph("C:\\albania-noder", "C:\\albania-kanter", albania_names)

    node_korce = albania_graph.nodes[36658]  # Korçë
    node_vlore = albania_graph.nodes[43011]  # Vlorë

    test_astar_dijkstra(albania_graph, node_korce, node_vlore)


    skandinavia_names = import_names("C:\\skandinavia-interessepkt")
    skandinavia_graph = import_astar_graph("C:\\skandinavia-noder", "C:\\skandinavia-kanter", skandinavia_names)

    node_trondheim = skandinavia_graph.nodes[347370]
    node_oslo = skandinavia_graph.nodes[143917]

    test_astar_dijkstra(skandinavia_graph, node_trondheim, node_oslo, True)
