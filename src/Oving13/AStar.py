import math
from AStarMinHeap import AStarMinHeap
from AStarGraph import AStarGraphNode, AStarGraph


def haversine(l1, b1, l2, b2):
    l1 = math.radians(l1)
    b1 = math.radians(b1)
    l2 = math.radians(l2)
    b2 = math.radians(b2)

    return 12742000 * math.asin(math.sqrt(
        math.sin((b1 - b2) / 2) ** 2 + math.cos(b1) * math.cos(b2) * math.sin((l1 - l2) / 2) ** 2
    ))


def astar(graph: AStarGraph, start_node: AStarGraphNode, end_node: AStarGraphNode):
    # Reset nodes
    for node in graph.nodes:
        node.dist = math.inf
        node.prio = math.inf
        node.predecessor = None

    start_node.dist = 0
    start_node.prio = 0

    # Make priority queue
    pri_queue = AStarMinHeap(graph)

    while pri_queue.len > 0 and pri_queue.nodes[0] is not end_node:  # Cancel when end node is to be removed from queue
        node = pri_queue.pop_min()
        for edge in node.edges:
            # Check if we haven't calculated estimated distance to end node yet
            if edge.to_node.est_dist < 0:
                lat = edge.to_node.lat
                long = edge.to_node.long
                edge.to_node.est_dist = 360 * haversine(lat, long, end_node.lat, end_node.long) / 110

            if edge.to_node.dist > node.dist + edge.weight:
                edge.to_node.dist = node.dist + edge.weight
                new_prio = edge.to_node.dist + edge.to_node.est_dist
                edge.to_node.predecessor = node
                pri_queue.set_prio(edge.to_node.heap_pos, new_prio)
