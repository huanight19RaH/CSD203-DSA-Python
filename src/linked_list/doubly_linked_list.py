class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

DNode = Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def check_empty(self):
        return self.head is None

    def isEmpty(self):
        return self.check_empty()

    def length(self):
        if self.head is None:
            return 0
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def __len__(self):
        return self.length()

    def insertLast(self, val):
        newNode = Node(val)
        if self.check_empty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def append(self, val):
        self.insertLast(val)

    def insertFirst(self, val):
        newNode = Node(val)
        if self.check_empty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def prepend(self, val):
        self.insertFirst(val)

    def removeFirst(self):
        if self.check_empty():
            print("Empty")
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def removeLast(self):
        if self.check_empty():
            print("Empty")
            return
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def removeValue(self, val):
        if self.check_empty():
            print("Empty")
            return False
        if self.head.data == val:
            self.removeFirst()
            return True
        elif self.tail.data == val:
            self.removeLast()
            return True
        else:
            current = self.head
            while current is not None:
                if current.data == val:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    return True
                current = current.next
        return False

    def delete(self, key):
        return self.removeValue(key)

    def display(self):
        if self.check_empty():
            print("Empty list")
            return
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def forward_traverse(self):
        self.display()

    def backward_traverse(self):
        if self.check_empty():
            print("Empty list")
            return
        current = self.tail
        while current is not None:
            print(current.data, end=" ")
            current = current.prev
        print()
