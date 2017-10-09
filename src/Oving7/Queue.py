from LinkedList import LinkedList


class Queue(LinkedList):
    def enqueue(self, value):
        return self.add(value)

    def dequeue(self):
        node = self.head
        self.head = self.head.next
        return node

    def empty(self):
        return self.head is None
