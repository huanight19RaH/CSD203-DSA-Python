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
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def insertProduct(self, id, name, price):
        if name.startswith("G") or id > 100 or price > 100:
            return
        prod = Product(id, name, price)
        self.root = self._insertRec(self.root, prod)

    def _insertRec(self, node, prod):
        if node is None:
            return Node(prod)
        if prod.id < node.data.id:
            node.left = self._insertRec(node.left, prod)
        elif prod.id > node.data.id:
            node.right = self._insertRec(node.right, prod)
        return node

    def f2(self, x):
        self._inOrderLessThanX(self.root, x)
        print()

    def _inOrderLessThanX(self, node, x):
        if node is None:
            return
        self._inOrderLessThanX(node.left, x)
        if node.data.price < x:
            print(node.data, end = " ")
        self._inOrderLessThanX(node.right, x)
