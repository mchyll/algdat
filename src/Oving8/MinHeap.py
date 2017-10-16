def parent_index(node_index):
    return (node_index - 1) >> 1


def left_child_index(node_index):
    return (node_index << 1) + 1


def right_child_index(node_index):
    return (node_index + 1) << 1


def make_min_heap(arr):
    heap = MinHeap()
    heap.nodes = list(arr)
    heap.len = len(heap.nodes)
    heap.create_heap()
    return heap


class HeapNode:
    priority = 0
    data = None

    def __init__(self, pri, data):
        self.priority = pri
        self.data = data


# Min-Heap sp
class MinHeap:
    len = 0
    nodes = []

    def fix_heap(self, index):
        child_to_swap = left_child_index(index)
        if child_to_swap < self.len:
            right_child = child_to_swap + 1

            if right_child < self.len and self.nodes[right_child].priority < self.nodes[child_to_swap].priority:
                child_to_swap = right_child

            if self.nodes[child_to_swap].priority < self.nodes[index].priority:
                self.nodes[index], self.nodes[child_to_swap] = self.nodes[child_to_swap], self.nodes[index]
                # Dijkstra needs to know the positions of nodes in the heap
                self.nodes[index].data.heap_pos = child_to_swap
                self.nodes[child_to_swap].data.heap_pos = index
                self.fix_heap(child_to_swap)

    def create_heap(self):
        index = self.len >> 1
        while index > 0:
            index -= 1
            self.fix_heap(index)

    def pop_min(self):
        min = self.nodes[0]
        self.len -= 1
        self.nodes[0] = self.nodes[self.len]
        self.fix_heap(0)
        return min

    def decrease_pri(self, index, pri):
        self.nodes[index].priority -= pri
        parent = parent_index(index)
        while index > 0 and self.nodes[index].priority < self.nodes[parent].priority:
            self.nodes[index], self.nodes[parent] = self.nodes[parent], self.nodes[index]
            # Dijkstra needs to know the positions of nodes in the heap
            self.nodes[index].data.heap_pos = parent
            self.nodes[parent].data.heap_pos = index
            index = parent
            parent = parent_index(index)

    def increase_pri(self, index, pri):
        self.nodes[index].priority += pri
        self.fix_heap(index)

    def set_pri(self, index, pri):
        delta = pri - self.nodes[index].priority
        if delta > 0:
            self.increase_pri(index, delta)
        elif delta < 0:
            self.decrease_pri(index, -delta)

    def insert(self, pri, data):
        node = HeapNode(pri, data)
        self.len += 1
        if len(self.nodes) <= self.len:
            self.nodes.append(node)
            self.len = len(self.nodes)
        else:
            self.nodes[self.len - 1] = node

        self.nodes[self.len - 1].data.heap_pos = self.len - 1
        self.decrease_pri(self.len - 1, 0)


if __name__ == "__main__":
    test = make_min_heap([
        HeapNode(7, "Me"),
        HeapNode(9, "Hello"),
        HeapNode(10, "Is"),
        HeapNode(8, "It"),
        HeapNode(6, "You're"),
        HeapNode(4, "For"),
        HeapNode(5, "Looking"),
    ])
    for i in range(test.len):
        min = test.pop_min()
        print("{}: {}".format(min.priority, min.data))
