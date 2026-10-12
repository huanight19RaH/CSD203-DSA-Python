"""
CSD203 - Doubly Linked List Implementation
Bidirectional sequential access with next and prev pointers.
"""

class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        return self._size

    def append(self, data):
        """Append node to tail in O(1)."""
        new_node = DNode(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, data):
        """Prepend node to head in O(1)."""
        new_node = DNode(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def delete(self, key):
        """Delete first occurrence of key in O(n)."""
        current = self.head
        while current is not None:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self._size -= 1
                return True
            current = current.next
        return False

    def forward_traverse(self):
        """Print elements from head to tail."""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements))

    def backward_traverse(self):
        """Print elements from tail to head."""
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
        print(" <-> ".join(elements))
