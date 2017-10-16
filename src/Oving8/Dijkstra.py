import math
from BFS import bfs
from DijkstraMinHeap import DijkstraMinHeap, print_heap
from Graph import import_graph
from WeightedGraph import import_weighted_graph, WeightedGraphNode, WeightedGraph


def dijkstra(graph: WeightedGraph, start_node: WeightedGraphNode, end_node: WeightedGraphNode = None):
    # Reset nodes
    for node in graph.nodes:
        node.dist = math.inf
        node.predecessor = None
    start_node.dist = 0

    # Make priority queue
    pri_queue = DijkstraMinHeap(graph)
    # print()

    while pri_queue.len > 0 and pri_queue.nodes[0] is not end_node:  # Cancel when end node is to be removed from queue
        # print_heap(pri_queue)
        node = pri_queue.pop_min()
        # print("Current: {}, dist: {}".format(node.label, node.dist))
        for edge in node.edges:
            # print("  neighbor: {}, weight: {}, heap_pos: {}, neighbor.dist: {}, dist+weight: {}".format(
            #    edge.to_node.label, edge.weight, edge.to_node.heap_pos, edge.to_node.dist, node.dist + edge.weight))
            if edge.to_node.dist > node.dist + edge.weight:
                # print_heap(pri_queue)
                edge.to_node.dist = node.dist + edge.weight
                edge.to_node.predecessor = node
                pre = edge.to_node.heap_pos
                pri_queue.dist_decreased(edge.to_node.heap_pos)
                # print("    Moved neighbor from heap_pos {} to {}".format(pre, edge.to_node.heap_pos))
        # print()


if __name__ == "__main__":
    names = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}
    names = {}
    graph = import_weighted_graph("C:\\vg3", names)
    dijkstra(graph, graph.nodes[1])
    print("\nNode    Pred.   Dist.")
    for node in graph.nodes:
        predecessor = " " if node.predecessor is None else node.predecessor.label
        print("{:>4}{:>8}{:>8}".format(node.label, predecessor, node.dist))

    """
    graph = import_graph("C:\\vg1")
    bfs(graph, graph.nodes[1])
    print("\nNode    Pred.   Hops")
    for node in graph.nodes:
        predecessor = " " if node.predecessor is None else node.predecessor.label
        print("{:4}{:8}{:8}".format(node.label, predecessor, node.dist))
    """
