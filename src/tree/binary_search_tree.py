"""
CSD203 - Binary Search Tree (BST) Implementation
Comprehensive BST supporting Traversals (In/Pre/Post/Breadth-First),
Deletion (by Copying and by Merging), Property analysis, and FPT Exam queries.
"""

from collections import deque

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"({self.id}, {self.name}, {self.price})"

    def __repr__(self):
        return self.__str__()


class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    # --- Core BST Operations ---

    def insert(self, val):
        """Insert generic value/object into BST."""
        self.root = self._insert_rec(self.root, val)

    def _insert_rec(self, node, val):
        if node is None:
            return BSTNode(val)
        val_key = val.id if hasattr(val, 'id') else val
        node_key = node.data.id if hasattr(node.data, 'id') else node.data

        if val_key < node_key:
            node.left = self._insert_rec(node.left, val)
        elif val_key > node_key:
            node.right = self._insert_rec(node.right, val)
        return node

    def search(self, key):
        """Search node by key. Returns node or None."""
        current = self.root
        while current:
            curr_key = current.data.id if hasattr(current.data, 'id') else current.data
            if curr_key == key:
                return current
            elif key < curr_key:
                current = current.left
            else:
                current = current.right
        return None

    # --- Traversals ---

    def in_order(self, node=None, is_root=True):
        """LNR (In-Order) Traversal."""
        if is_root:
            node = self.root
        result = []
        if node:
            result.extend(self.in_order(node.left, False))
            result.append(node.data)
            result.extend(self.in_order(node.right, False))
        return result

    def pre_order(self, node=None, is_root=True):
        """NLR (Pre-Order) Traversal."""
        if is_root:
            node = self.root
        result = []
        if node:
            result.append(node.data)
            result.extend(self.pre_order(node.left, False))
            result.extend(self.pre_order(node.right, False))
        return result

    def post_order(self, node=None, is_root=True):
        """LRN (Post-Order) Traversal."""
        if is_root:
            node = self.root
        result = []
        if node:
            result.extend(self.post_order(node.left, False))
            result.extend(self.post_order(node.right, False))
            result.append(node.data)
        return result

    def breadth_first(self):
        """BFS (Level-Order) Traversal using Queue."""
        if self.isEmpty():
            return []
        result = []
        queue = deque([self.root])
        while queue:
            curr = queue.popleft()
            result.append(curr.data)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return result

    # --- Properties ---

    def height(self, node=None, is_root=True):
        """Calculate height of tree."""
        if is_root:
            node = self.root
        if node is None:
            return 0
        return 1 + max(self.height(node.left, False), self.height(node.right, False))

    def count_nodes(self, node=None, is_root=True):
        """Count total nodes in tree."""
        if is_root:
            node = self.root
        if node is None:
            return 0
        return 1 + self.count_nodes(node.left, False) + self.count_nodes(node.right, False)

    # --- Deletion: By Copying ---

    def delete_by_copying(self, key):
        """Delete node by copying predecessor's data (CSD standard)."""
        self.root = self._delete_by_copying_rec(self.root, key)

    def _delete_by_copying_rec(self, node, key):
        if node is None:
            return None
        node_key = node.data.id if hasattr(node.data, 'id') else node.data
        if key < node_key:
            node.left = self._delete_by_copying_rec(node.left, key)
        elif key > node_key:
            node.right = self._delete_by_copying_rec(node.right, key)
        else:
            # Case 1 & 2: 0 or 1 child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Case 3: 2 children - find max in left subtree (predecessor)
            predecessor = node.left
            while predecessor.right:
                predecessor = predecessor.right
            node.data = predecessor.data
            node.left = self._delete_by_copying_rec(node.left, predecessor.data.id if hasattr(predecessor.data, 'id') else predecessor.data)
        return node

    # --- FPT Practical Exam Methods ---

    def insertProduct(self, id, name, price):
        """Exam specific: insert if name not starting with 'G', id <= 100, price <= 100."""
        if name.startswith("G") or id > 100 or price > 100:
            return
        prod = Product(id, name, price)
        self.insert(prod)

    def f2(self, x):
        """Exam specific: In-order traversal printing items where price < x."""
        self._inOrderLessThanX(self.root, x)
        print()

    def _inOrderLessThanX(self, node, x):
        if node is None:
            return
        self._inOrderLessThanX(node.left, x)
        if hasattr(node.data, 'price') and node.data.price < x:
            print(node.data, end=" ")
        self._inOrderLessThanX(node.right, x)
