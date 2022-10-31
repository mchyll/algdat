from typing import *
from queue import deque


class Node:
    def __init__(self, name):
        self.name = name
        self.edges: List[Edge] = []
        self.predecessorEdge: Optional[Edge] = None

    def __str__(self):
        return f"Node {self.name}, edges:" + "".join(["\n\t" + str(e) for e in self.edges]) + "\n"
    
    def getEdgeTo(self, node: "Node"):
        for edge in self.edges:
            if edge.toNode is node:
                return edge
        return None


class Edge:
    num = 0

    def __init__(self, fromNode: Node, toNode: Node, capacity: int):
        self.num = Edge.num
        Edge.num += 1
        self.reverse: Edge = None
        self.flow: int = 0
        self.capacity: int = capacity
        self.fromNode: Node = fromNode
        self.toNode: Node = toNode
    
    def __str__(self):
        return f"<{self.num}> Edge from {self.fromNode.name} to {self.toNode.name}, capacity {self.capacity}, reverse <{self.reverse.num}>"


def import_weighted_graph(filename, names=None):
    if names is None:
        names = {}

    graph: List[Node] = []
    with open(filename, "r", encoding="utf-8") as graph_file:
        num_line = graph_file.readline().split()
        num_nodes, num_edges = int(num_line[0]), int(num_line[1])
        print("{} nodes, {} edges".format(num_nodes, num_edges))

        graph = [None] * num_nodes

        print("Generating node objects...")
        for i in range(num_nodes):
            name = names[i] if i in names else i
            node = Node(name)
            graph[i] = node

        print("Reading edge entries...")
        for raw_line in graph_file:
            parts = raw_line.split()
            from_node = int(parts[0])
            to_node = int(parts[1])
            weight = int(parts[2])
            graph[from_node].edges.append(Edge(graph[from_node], graph[to_node], weight))

        print("Creating reverse edges...")
        for node in graph:
            for edge in node.edges.copy():
                neighbor: Node = edge.toNode
                rev = neighbor.getEdgeTo(node)
                if rev is None:
                    rev = Edge(neighbor, node, 0)
                edge.reverse = rev
                rev.reverse = edge
                neighbor.edges.append(rev)

    print("Graph generated")
    return graph


def edmonds_karp(graph: List[Node], s: Node, t: Node):
    maxflow = 0

    while True:
        for node in graph:
            node.predecessorEdge = None

        # BFS
        q = deque()
        q.append(s)
        while len(q) != 0:
            current: Node = q.popleft()
            for edge in current.edges:
                neighbor = edge.toNode
                if neighbor.predecessorEdge is None and neighbor is not s and edge.capacity > edge.flow:
                    neighbor.predecessorEdge = edge
                    q.append(neighbor)

        # If we found an augmenting path from source to sink
        if t.predecessorEdge is not None:
            # Check all edges in the augmenting path for the minimum rest capacity
            restCapacity = 999999999
            edge: Edge = t.predecessorEdge
            while edge is not None:
                restCapacity = min(restCapacity, edge.capacity - edge.flow)
                edge = edge.fromNode.predecessorEdge

            # Update the flow of all edges along the path
            edge: Edge = t.predecessorEdge
            path = []
            path.append(edge.toNode.name)
            while edge is not None:
                path.append(edge.fromNode.name)
                edge.flow += restCapacity
                edge.reverse.flow -= restCapacity
                edge = edge.fromNode.predecessorEdge

            path.reverse()
            print("Found augmenting path which increases the flow by {}: {}".format(restCapacity, " ".join([str(n) for n in path])))
            maxflow += restCapacity

        # If we didn't find a new augmenting path from source to sink, we're done
        else:
            break

    return maxflow


graph = import_weighted_graph("flytgraf3.txt")
print("".join([str(n) for n in graph]))

s = graph[0]
t = graph[1]
print("Max flow: {}".format(edmonds_karp(graph, s, t)))
