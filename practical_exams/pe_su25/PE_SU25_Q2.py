class Model:
    def __init__(self, name, month, year):
        self.name = name
        self.month = month
        self.year = year
    
    def compareTo(self, other):
        if self.year < other.year:
            return True
        elif self.year > other.year:
            return False
        else:
            if self.month < other.month:
                return True
            elif self.month > other.month:
                return False
            else:
                if self.name < other.name:
                    return True
                elif self.name > other.name:
                    return False
    
class BSTNode:
    def __init__(self, model):
        self.model = model
        self.left = None
        self.right  = None

class BSTree:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root is None
    
    def insert(self, model):
        if self.isEmpty():
            self.root = BSTNode(model)
        else:
            self._insert_recursive(self.root, model)

    def _insert_recursive(self, current, model):
        if model.compareTo(current.model): 
            if current.left is None:
                current.left = BSTNode(model)
            else:
                self._insert_recursive(current.left, model)
        else: 
            if current.right is None:
                current.right = BSTNode(model)
            else:
                self._insert_recursive(current.right, model)
       
    def in_order(self, node):
        if node is None:
            return
        else:
            self.in_order(node.left)
            print(f"{node.model.name} - {node.model.month}/{node.model.year}")
            self.in_order(node.right)
    
    def in_order_traverse(self):
        if self.isEmpty():
            print("Empty Tree")
            return
        else:
            self.in_order(self.root)
    
    def find_most_right(self, node):
        while node is not None and node.right is not None:
            node = node.right
        return node
    
    def delete_by_copyingRec(self, name, node):
        if node is None:
            return node
        else:
            if name < node.model.name: 
                node.left = self.delete_by_copyingRec(name, node.left)
            elif name > node.model.name: 
                node.right = self.delete_by_copyingRec(name, node.right)
            else: 
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                mostRight = self.find_most_right(node.left)
                node.model = mostRight.model 
                node.left = self.delete_by_copyingRec(mostRight.model.name, node.left)
            return node

    def delete_by_copying(self, name):
        if self.isEmpty():
            print("Empty Tree")
        else:
            self.root = self.delete_by_copyingRec(name, self.root)
            print()

    def search(self, name):
        node = self.root
        while node is not None:
            if node.model.name == name:
                print("Found")
                print(f"{node.model.name} - {node.model.month}/{node.model.year}")
                return node.model
            elif node.model.name < name:
                node = node.right
            else:
                node = node.left
        print("Not found")
        return None

BSTree1 = BSTree()

BSTree1.insert(Model('FLAN', 9, 2021))
BSTree1.insert(Model('BERT', 10, 2018))
BSTree1.insert(Model('Transformers', 6, 2017))
BSTree1.insert(Model('ChatGPT', 11, 2022))
BSTree1.insert(Model('GPT-3', 5, 2020))
BSTree1.insert(Model('GPT', 6, 2018))
BSTree1.insert(Model('GPT-2', 2, 2019))
BSTree1.insert(Model('DeepSeek_R1', 1, 2025))
BSTree1.insert(Model('GPT-4o', 3, 2024))
BSTree1.insert(Model('LLaMA', 2, 2023))
BSTree1.in_order_traverse()

BSTree1.delete_by_copying("LLaMA")
BSTree1.in_order_traverse()
BSTree1.search("FLAN")