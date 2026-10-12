"""
CSD203 - Queue Implementations
Standard FIFO Queue and Linked-List based PriorityQueue.
"""

class QueueNode:
    def __init__(self, data, priority=0):
        self.data = data
        self.priority = priority
        self.next = None


class Queue:
    """Standard FIFO Queue using linked nodes."""
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        return self._size

    def enqueue(self, val):
        new_node = QueueNode(val)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty queue")
        val = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self._size -= 1
        return val

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.data


class PriorityQueue:
    """Priority Queue where higher priority items are served first."""
    def __init__(self):
        self.head = None
        self._size = 0

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        return self._size

    def enqueue(self, val, priority=0):
        new_node = QueueNode(val, priority)
        if self.isEmpty() or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.priority >= priority:
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Dequeue from empty priority queue")
        val = self.head.data
        self.head = self.head.next
        self._size -= 1
        return val
