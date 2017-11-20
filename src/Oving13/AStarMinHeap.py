def parent_index(node_index):
    return (node_index - 1) >> 1


def left_child_index(node_index):
    return (node_index << 1) + 1


def right_child_index(node_index):
    return (node_index + 1) << 1


# Min-Heap for use in A* algorithm
class AStarMinHeap:
    len = 0
    nodes = []

    def __init__(self, graph):
        self.nodes = list(graph.nodes)
        self.len = len(graph.nodes)
        for i in range(self.len):
            self.nodes[i].heap_pos = i
        self.init_heap()

    def swap(self, a, b):
        self.nodes[a].heap_pos = b
        self.nodes[b].heap_pos = a
        self.nodes[a], self.nodes[b] = self.nodes[b], self.nodes[a]

    # Checks if a node is too far up in the heap, and swaps it downwards to its correct position
    def fix_heap(self, index):
        child_to_swap = left_child_index(index)
        if child_to_swap < self.len:
            right_child = child_to_swap + 1

            if right_child < self.len and self.nodes[right_child].prio < self.nodes[child_to_swap].prio:
                child_to_swap = right_child

            if self.nodes[child_to_swap].prio < self.nodes[index].prio:
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

    # Checks if a node is too far down in the heap, and swaps it upwards to its correct position
    def prio_decreased(self, index):
        parent = parent_index(index)
        while index > 0 and self.nodes[index].prio < self.nodes[parent].prio:
            self.swap(index, parent)
            index = parent
            parent = parent_index(index)

    # Same as fix_heap(index)
    def prio_increased(self, index):
        self.fix_heap(index)

    def set_prio(self, index, prio):
        delta = prio - self.nodes[index].prio
        self.nodes[index].prio = prio
        if delta > 0:
            self.prio_increased(index)
        elif delta < 0:
            self.prio_decreased(index)

    def insert(self, node):
        self.len += 1
        if len(self.nodes) <= self.len:
            self.nodes.append(node)
            self.len = len(self.nodes)
        else:
            self.nodes[self.len - 1] = node

        self.nodes[self.len - 1].heap_pos = self.len - 1
        self.prio_decreased(self.len - 1)
