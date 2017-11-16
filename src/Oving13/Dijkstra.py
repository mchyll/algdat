import math
from DijkstraMinHeap import DijkstraMinHeap
from WeightedGraph import import_weighted_graph, WeightedGraphNode, WeightedGraph


def dijkstra(graph: WeightedGraph, start_node: WeightedGraphNode, end_node: WeightedGraphNode = None):
    # Reset nodes
    for node in graph.nodes:
        node.dist = math.inf
        node.predecessor = None
    start_node.dist = 0

    # Make priority queue
    pri_queue = DijkstraMinHeap(graph)

    while pri_queue.len > 0 and pri_queue.nodes[0] is not end_node:  # Cancel when end node is to be removed from queue
        node = pri_queue.pop_min()
        for edge in node.edges:
            if edge.to_node.dist > node.dist + edge.weight:
                edge.to_node.dist = node.dist + edge.weight
                edge.to_node.predecessor = node
                pri_queue.dist_decreased(edge.to_node.heap_pos)


if __name__ == "__main__":
    graph = import_weighted_graph("C:\\vg3")
    dijkstra(graph, graph.nodes[1])
    print("\nNode    Pred.   Dist.")
    for node in graph.nodes:
        predecessor = " " if node.predecessor is None else node.predecessor.label
        print("{:>4}{:>8}{:>8}".format(node.label, predecessor, node.dist))
