import math
from MinHeap import MinHeap
from WeightedGraph import import_weighted_graph, WeightedGraphNode, WeightedGraph


def dijkstra(graph: WeightedGraph, start_node: WeightedGraphNode):
    # Reset nodes and make priority queue
    pri_queue = MinHeap()
    for node in graph.nodes:
        node.dist = math.inf
        if node is start_node:
            node.dist = 0
        node.predecessor = None
        pri_queue.insert(node.dist, node)

    while pri_queue.len > 0:
        node = pri_queue.pop_min().data
        print("Current: {}".format(node.label))
        for edge in node.edges:
            print("    neighbor: {}".format(node.label))
            if edge.to_node.dist > node.dist + edge.weight:
                dist_delta = edge.to_node.dist - node.dist - edge.weight
                edge.to_node.dist = node.dist + edge.weight
                edge.to_node.predecessor = node
                pri_queue.decrease_pri(edge.to_node.heap_pos, dist_delta)


if __name__ == "__main__":
    graph = import_weighted_graph("C:\\vg1")
    dijkstra(graph, graph.nodes[1])
    print("\nNode    Pred.   Dist.")
    for node in graph.nodes:
        predecessor = " " if node.predecessor is None else node.predecessor.label
        print("{:4}{:8}{:8}".format(node.label, predecessor, node.dist))
