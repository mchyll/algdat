from LinkedList import LinkedList


class Queue(LinkedList):
    def enqueue(self, value):
        return self.add(value)

    def dequeue(self):
        node = self.head
        if node is None:
            return None

        self.head = self.head.next
        return node.value

    def empty(self):
        return self.head is None
