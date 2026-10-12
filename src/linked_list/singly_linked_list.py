"""
CSD203 - Singly Linked List Implementation
Includes generic LinkedList operations and FPT Practical Exam problem functions (f1, f2, f3, f4).
"""

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"({self.id}, {self.name}, {self.price})"

    def __repr__(self):
        return self.__str__()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyList:
    """
    Singly Linked List tailored for CSD203 coursework and practical exams.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # --- Standard Linked List Operations ---

    def append(self, data):
        """Add node to the end of the list."""
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Add node to the beginning of the list."""
        new_node = Node(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        """Print all elements in list."""
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def to_list(self):
        """Convert linked list elements into Python list."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        """Reverse the linked list in-place (O(n))."""
        prev = None
        current = self.head
        self.tail = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # --- FPT Practical Exam Functions (f1 - f4) ---

    def f1(self, id, name, price):
        """
        f1: Insert a new Product into tail if condition met
        (name does not start with 'C', id >= 0, price >= 0).
        Fixed NameError bug from original exam template.
        """
        if name.startswith("C") or id < 0 or price < 0:
            return
        new_product = Product(id, name, price)
        newNode = Node(new_product)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def f2(self, A):
        """
        f2: Insert item A before the 2nd product having an even ID.
        If fewer than 2 even IDs exist, append to tail.
        """
        current = self.head
        count_even = 0
        prev = None

        while current is not None:
            if hasattr(current.data, 'id') and current.data.id % 2 == 0:
                count_even += 1
                if count_even == 2:
                    break
            prev = current
            current = current.next

        newNode = Node(A)
        if count_even < 2:
            if self.tail is not None:
                self.tail.next = newNode
                self.tail = newNode
            else:
                self.head = self.tail = newNode
        elif prev is None:
            newNode.next = self.head
            self.head = newNode
        else:
            newNode.next = prev.next
            prev.next = newNode

    def f3(self, x):
        """
        f3: Delete the first product whose price is strictly greater than x.
        """
        current = self.head
        prev = None
        while current is not None:
            if hasattr(current.data, 'price') and current.data.price > x:
                if prev is None:
                    self.head = current.next
                    if current == self.tail:
                        self.tail = None
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev
                return
            prev = current
            current = current.next

    def f4(self):
        """
        f4: Sort products having an even ID by price ascending,
        leaving other nodes in place.
        """
        p = self.head
        while p:
            if hasattr(p.data, 'id') and p.data.id % 2 == 0:
                q = p.next
                while q:
                    if hasattr(q.data, 'id') and q.data.id % 2 == 0 and q.data.price < p.data.price:
                        p.data, q.data = q.data, p.data
                    q = q.next
            p = p.next
