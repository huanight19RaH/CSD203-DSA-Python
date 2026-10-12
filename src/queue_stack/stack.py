"""
CSD203 - Stack Implementation
LIFO (Last-In, First-Out) sequential container.
"""

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top_node = None
        self._size = 0

    def isEmpty(self):
        return self.top_node is None

    def __len__(self):
        return self._size

    def push(self, val):
        new_node = StackNode(val)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Pop from empty stack")
        val = self.top_node.data
        self.top_node = self.top_node.next
        self._size -= 1
        return val

    def top(self):
        if self.isEmpty():
            return None
        return self.top_node.data
