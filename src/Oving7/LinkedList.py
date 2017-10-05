class LinkedList:
    head = None
    tail = None

    def add(self, value):
        new_node = LinkedListNode(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return new_node

        self.tail.next = new_node
        self.tail = new_node
        return new_node

    def remove(self, node):
        if self.head is None or node is None:
            return

        if node is self.head:
            if self.head is self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next

        else:
            prev = self.head
            current = self.head.next
            while current is not node and current is not None:
                prev = current
                current = current.next

            if current is not None:
                prev.next = current.next
                if current is self.tail:
                    self.tail = prev

    def print_list(self):
        node = self.head
        head = None if self.head is None else self.head.value
        tail = None if self.tail is None else self.tail.value
        print("Head = {}, tail = {}    ".format(head, tail), end='')
        while node is not None:
            print("{} -> ".format(node.value), end='')
            node = node.next
        print()


class UnorderedLinkedList:
    head = None

    def add(self, value):
        new_node = LinkedListNode(value, self.head)
        self.head = new_node
        return new_node

    def remove(self, node):
        prev = self.head
        current = self.head.next
        while current is not node and current is not None:
            prev = current
            current = current.next

        if current is not None:
            if prev is not None:
                prev.next = current.next
            else:
                self.head = current.next

    def size(self):
        i = 0
        current = self.head
        while current is not None:
            i += 1
            current = current.next

        return i

    def print_list(self):
        node = self.head
        head = None if self.head is None else self.head.value
        print("Head = {}    ".format(head), end='')
        while node is not None:
            print("{} -> ".format(node.value), end='')
            node = node.next
        print()


class LinkedListNode:
    next = None
    value = None

    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def get_nth_next(self, n):
        result = self
        while n > 0 and result is not None:
            result = result.next
            n -= 1
        return result


if __name__ == "__main__":
    list = LinkedList()
    a = list.add("a")
    b = list.add("b")
    c = list.add("c")
    d = list.add("d")
    e = list.add("e")
    f = list.add("f")
    list.print_list()

    list.remove(a)
    list.print_list()

    list.remove(a)
    list.print_list()

    list.remove(f)
    list.print_list()

    list.remove(d)
    list.print_list()

    list.remove(c)
    list.print_list()

    list.remove(b)
    list.print_list()

    list.remove(e)
    list.print_list()
