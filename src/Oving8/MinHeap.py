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


class MinHeap:
    len = 0
    nodes = []

    def fix_heap(self, index):
        left = left_child_index(index)
        if left < self.len:
            right = left + 1

            if right < self.len and self.nodes[right].priority < self.nodes[left].priority:
                left = right

            if self.nodes[left].priority < self.nodes[index].priority:
                self.nodes[index], self.nodes[left] = self.nodes[left], self.nodes[index]
                self.fix_heap(left)

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
            index = parent
            parent = parent_index(index)

    def increase_pri(self, index, pri):
        self.nodes[index].priority += pri
        self.fix_heap(index)

    def insert(self, pri, data):
        node = HeapNode(pri, data)
        self.len += 1
        if len(self.nodes) <= self.len:
            self.nodes.append(node)
        else:
            self.nodes[self.len - 1] = node
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
