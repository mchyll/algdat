class CircularDoublyLinkedList:
    head = None
    len = 0

    def add(self, value):
        element = DoublyLinkedNode(value)

        if self.head is None:
            element.prev = element
            element.next = element
            self.head = element
            self.len += 1
            return element

        first = self.head
        last = first.prev
        last.next = element
        element.prev = last
        element.next = first
        first.prev = element
        self.len += 1
        return element

    def remove(self, element):
        if self.len == 0:
            return

        if element is self.head:
            last = self.head.prev
            last.next = self.head.next
            self.head.next.prev = last
            self.len -= 1
            if self.len == 0:
                self.head = None
            else:
                self.head = self.head.next
            return

        right, left = element.next, element.prev
        right.prev = left
        left.next = right
        self.len -= 1

    def print_list(self):
        node = self.head
        for i in range(self.len):
            print("{} -> ".format(node.value), end='')
            node = node.next
        print()


class DoublyLinkedNode:
    prev = None
    next = None
    value = None

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def get_nth_next(self, n):
        result = self
        while n > 0:
            result = result.next
            n -= 1
        return result


liste = CircularDoublyLinkedList()
antall = 20
intervall = 4

for i in range(antall):
    liste.add(str(i + 1))

liste.print_list()
kill = liste.head.get_nth_next(intervall - 1)  # Førstemann som drepes
while liste.len > 1:
    liste.remove(kill)
    print("Drepte {}".format(kill.value))
    liste.print_list()
    kill = kill.get_nth_next(intervall)

print("Josephus må stå på posisjon {}".format(liste.head.value))

"""
Kompleksiteten blir O(n * k), hvor n er antall soldater
og k er intervallet mellom hver som drepes
"""
