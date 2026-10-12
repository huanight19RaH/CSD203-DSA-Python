"""
CSD203 - AVL Tree (Self-Balancing Binary Search Tree)
Maintains O(log n) guaranteed search, insert, and delete through rotation.
"""

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def right_rotate(self, z):
        """Right rotation around node z."""
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def left_rotate(self, z):
        """Left rotation around node z."""
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, key):
        self.root = self._insert_rec(self.root, key)

    def _insert_rec(self, node, key):
        # 1. Standard BST insertion
        if not node:
            return AVLNode(key)
        elif key < node.key:
            node.left = self._insert_rec(node.left, key)
        elif key > node.key:
            node.right = self._insert_rec(node.right, key)
        else:
            return node  # Duplicate keys not allowed

        # 2. Update height of current ancestor node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # 3. Get the balance factor
        balance = self.get_balance(node)

        # 4. Check if unbalanced and apply 4 rotation cases:
        # Case 1 - Left Left (LL)
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Case 2 - Right Right (RR)
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Case 3 - Left Right (LR)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Case 4 - Right Left (RL)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def in_order(self, node=None, is_root=True):
        if is_root:
            node = self.root
        res = []
        if node:
            res.extend(self.in_order(node.left, False))
            res.append(node.key)
            res.extend(self.in_order(node.right, False))
        return res
