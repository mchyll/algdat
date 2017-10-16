import math


def parent_index(node_index):
    return (node_index - 1) >> 1


def left_child_index(node_index):
    return (node_index << 1) + 1


def right_child_index(node_index):
    return (node_index + 1) << 1


def print_heap(heap, index=0):
    if index >= heap.len:
        return

    depth = int(math.log(index + 1, 2))
    print(" " * 4 * depth + "[{}]={}".format(heap.nodes[index].label, heap.nodes[index].dist))
    print_heap(heap, left_child_index(index))
    print_heap(heap, right_child_index(index))


# Min-Heap for use in Dijkstra's algorithm
class DijkstraMinHeap:
    len = 0
    nodes = []

    def __init__(self, graph):
        self.nodes = list(graph.nodes)
        self.len = len(graph.nodes)
        for i in range(self.len):
            self.nodes[i].heap_pos = i
        self.init_heap()

    def swap(self, a, b):
        # print(" " * 8 + "Swaps [{}]={} with [{}]={}".format(a, self.nodes[a].dist, b, self.nodes[b].dist))
        # Dijkstra needs to know the positions of nodes in the heap
        self.nodes[a].heap_pos = b
        self.nodes[b].heap_pos = a
        self.nodes[a], self.nodes[b] = self.nodes[b], self.nodes[a]

    # Checks if a node is too far up in the heap, and swaps it downwards to its correct position
    def fix_heap(self, index):
        child_to_swap = left_child_index(index)
        if child_to_swap < self.len:
            right_child = child_to_swap + 1

            if right_child < self.len and self.nodes[right_child].dist < self.nodes[child_to_swap].dist:
                child_to_swap = right_child

            if self.nodes[child_to_swap].dist < self.nodes[index].dist:
                self.swap(index, child_to_swap)
                self.fix_heap(child_to_swap)

    def init_heap(self):
        index = self.len >> 1
        while index > 0:
            index -= 1
            self.fix_heap(index)

    def pop_min(self):
        self.len -= 1
        self.swap(0, self.len)
        self.fix_heap(0)
        self.nodes[self.len].heap_pos = -1  # Not in the heap anymore
        return self.nodes[self.len]

    def dist_decreased(self, index):
        parent = parent_index(index)
        # print("HEAP: dist_decreased")
        # print("ser på [{}]={} og [{}]={}".format(index, self.nodes[index].dist, parent, self.nodes[parent].dist))
        while index > 0 and self.nodes[index].dist < self.nodes[parent].dist:
            # print("    {} < {}, må derfor swappes".format(self.nodes[index].dist, self.nodes[parent].dist))
            self.swap(index, parent)
            index = parent
            parent = parent_index(index)
            # print("ser på [{}]={} og [{}]={}".format(index, self.nodes[index].dist, parent, self.nodes[parent].dist))

    def dist_increased(self, index):
        self.fix_heap(index)

    def set_dist(self, index, dist):
        delta = dist - self.nodes[index].dist
        self.nodes[index].dist = dist
        if delta > 0:
            self.dist_increased(index)
        elif delta < 0:
            self.dist_decreased(index)

    def insert(self, node):
        self.len += 1
        if len(self.nodes) <= self.len:
            self.nodes.append(node)
            self.len = len(self.nodes)
        else:
            self.nodes[self.len - 1] = node

        self.nodes[self.len - 1].heap_pos = self.len - 1
        self.dist_decreased(self.len - 1)
