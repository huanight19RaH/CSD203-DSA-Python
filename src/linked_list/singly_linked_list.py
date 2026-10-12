class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"({self.id}, {self.name}, {self.price})"


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None

    def f1(self, id, name, price):
        if name.startswith("C") or id < 0 or price < 0:
            return
        new_product = Product(id, name, price)
        newNode = Node(new_product)
        if self.isEmpty():
            self.head = self.tail = newNode
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while currennt is not None:
            print(current.data, end = " ")
            current = current.next
        print()

    def f2(self, A):
        current = self.head
        count_even = 0
        prev = None

        while current is not None:
            if current.data.id % 2 == 0:
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
        current = self.head
        prev = None
        while current is not None:
            if current.data.price > x:
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
        p = self.head
        while p:
            if p.data.id % 2 == 0:
                q = p.next
                while q:
                    if q.data.id % 2 == 0 and q.data.price < p.data.price:
                        p.data, q.data = q.data, p.data
                    q = q.next
            p = p.next
