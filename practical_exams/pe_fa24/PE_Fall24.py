class Typhoon:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def __str__(self):
        return f"{self.name}:{self.country};"

class Node:
    def __init__(self, typhoon):
        self.typhoon = typhoon
        self.next = None

class BST_Node:
    def __init__(self, typhoon):
        self.typhoon = typhoon
        self.left = None
        self.right = None
    
class TyphoonLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def check_empty(self):
        return self.head is None
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
            
    def display(self):
        if self.check_empty():
            print("Empty list")
        else:
            current = self.head
            while current != None:
                print(current, end = "\n")
                current = current.next
            print()
            
    def insert(self, name, country, pos = None):
        newNode = Node(Typhoon(name, country))
        if self.check_empty():
            self.head = newNode
            self.tail = newNode
        else:
            if pos == None:
                self.tail.next = newNode
                self.tail = newNode
            elif pos >= self.length():
                raise ValueError("Position is out of range")
            elif pos == 0:
                newNode.next = self.head
                self.head = newNode
            else:
                current_pos = 0
                current = self.head
                while current_pos < pos - 1:
                    current = current.next
                    current_pos += 1
                newNode.next = current.next
                current.next = newNode
                
    def load_typhoon_data(self, filename):
        with open(filename, 'r', encoding = 'utf-8') as file:
            lines = file.readlines()
            for line in lines[1:]:
                typhoons = line.strip().split(',')
                #print(typhoons)
                country = typhoons[0]
                for typhoon in typhoons[1:]:
                    self.insert(typhoon, country)
                    
class TyphoonBST:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return self.root is None
    
    def preorder_traversal(self, node):
        if node is None:
            return
        else:
            print(node, end = "\n")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def display(self):
        if self.isEmpty():
            print("Empty Tree")
            print("\n" + 50 * "=")
        else:
            self.preorder_traversal(self.root)
            print("\n" + 50 * "=")
    
    def insertRec(self, name, country, node):
        if node is None:
            return BST_Node(Typhoon(name, country))
        if name < node.typhoon.name:
                node.left = self.insertRec(name, country, node.left)
        elif name > node.typhoon.name:
                node.right = self.insertRec(name, country, node.right)
        return node
    
    def insert(self, name, country):
        if self.isEmpty():
            self.root = BST_Node(Typhoon(name, country))
        else:
            self.root = self.insertRec(name, country, self.root)
    
    def delete_by_copyingRec(self, name, node):
        if node is None:
            return node
        else:
            if name > node.typhoon.name:
                node.right = self.delete_by_copyingRec(name, node.right)
            elif name < node.typhoon.name:
                node.left = self.delete_by_copyingRec(name, node.left)
            elif name == node.typhoon.name:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                mostRight = self.find_most_right(node.left)
                node.typhoon.name = mostRight.typhoon.name
                node.left = self.delete_by_copyingRec(mostRight.typhoon.name, node.left)
            return node
    
    def delete_by_copying(self, name):
        if self.isEmpty():
            print("Empty Tree")
        else:
            self.root = self.delete_by_copyingRec(name, self.root)
    
    def find_most_right(self, node):
        while node is not None and node.right is not None:
            node = node.right
        return node
    
    def search(self, name):
        node = self.root
        while node is not None:
            if node.typhoon.name == name:
                print(node.typhoon)
                return node
            if node.typhoon.name < name:
                node = node.right
            else:
                node = node.left
        print("Not found")
        return None

class AVLTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None
    
    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1
    
    def preorder_traversal(self, node):
        if node is None:
            return
        else:
            print(node, end = "\n")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    
    def display(self):
        if self.isEmpty():
            print("Empty Tree")
            print("\n" + 50 * "=")
        else:
            self.preorder_traversal(self.root)
            print("\n" + 50 * "=")
    
    def balance_cal(self, node):
        return self.height(node.left) - self.height(node.right)
    
    def right_rotate(self, node):
        a = node.left
        node.left = a.right
        a.right = node
        return a
    
    def left_rotate(self, node):
        a = node.right
        node.right = a.left
        a.left = node
        return a
    
    def insertRes(self, name, country):
        if self.isEmpty():
            self.root = BST_Node(Typhoon(name, country))
        else:
            self.root = self.insertRec(name, country, self.root)

    def insertRec(self, name, country, node):
        if node is None:
            return BST_Node(Typhoon(name, country))
        if name < node.typhoon.name:
            node.left = self.insertRec(name, country, node.left)
        elif name > node.typhoon.name:
            node.right = self.insertRec(name, country, node.right)
        #avlTree
        balance = self.balance_cal(node)
        if balance > 1: #height left subtree > height right subtree
            if self.balance_cal(node.left) < 0:
                node.left = self.left_rotate(node.left)
            node = self.right_rotate(node)
        elif balance < -1:
            if self.balance_cal(node.right) > 0:
                node.right = self.right_rotate(node.right)
            node = self.left_rotate(node)
        return node

    def delete_by_copyingRec(self, name, node):
        if node is None:
            return node
        else:
            if name > node.typhoon.name:
                node.right = self.delete_by_copyingRec(name, node.right)
            elif name < node.typhoon.name:
                node.left = self.delete_by_copyingRec(name, node.left)
            elif name == node.typhoon.name:
                if node.left is None and node.right is None:
                    return None
                elif node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                mostRight = self.find_most_right(node.left)
                node.typhoon.name = mostRight.typhoon.name
                node.left = self.delete_by_copyingRec(mostRight.typhoon.name, node.left)
            #avlTree
            balance = self.balance_cal(node)
            if balance > 1: #height left subtree > height right subtree
                if self.balance_cal(node.left) < 0:
                    node.left = self.left_rotate(node.left)
                node = self.right_rotate(node)
            elif balance < -1:
                if self.balance_cal(node.left) > 0:
                    node.right = self.right_rotate(node.right)
                node = self.left_rotate(node)
            return node
    
    def delete_by_copying(self, name):
        if self.isEmpty():
            print("Empty Tree")
        else:
            self.root = self.delete_by_copyingRec(name, self.root)
    
    def find_most_right(self, node):
        while node is not None and node.right is not None:
            node = node.right
        return node
    
    def find_most_left(self, node):
        while node is not None and node.left is not None:
            node = node.left
        return node
    
    def search(self, name):
        node = self.root
        while node is not None:
            if node.typhoon.name == name:
                print(node.typhoon)
                return node
            if node.typhoon.name < name:
                node = node.right
            else:
                node = node.left
        print("Not found")
        return None

def main():
    filename = 'typhoon_data.csv'
    #LinkedList
    typhoon_LL = TyphoonLinkedList()
    typhoon_LL.load_typhoon_data(filename)
    #BST
    typhoon_BST = TyphoonBST()
    current = typhoon_LL.head
    while current is not None:
        typhoon_BST.insert(current.typhoon.name, current.typhoon.country)
        current = current.next
    #AVL_Tree
    typhoon_AVL = AVLTree()
    current1 = typhoon_LL.head
    while current1 is not None:
        typhoon_AVL.insertRes(current1.typhoon.name, current1.typhoon.country)
        current1 = current1.next
    typhoon_AVL.search("Saola")

main()

    
'''filename = 'typhoon_data.csv'
typhoon_LL = TyphoonLinkedList()
typhoon_LL.load_typhoon_data('typhoon_data.csv')
#typhoon_LL.display()'''

'''typhoon_BST = TyphoonBST()
current = typhoon_LL.head
while current is not None:
    typhoon_BST.insert(current.name, current.country)
    current = current.next
typhoon_BST.delete_by_copying("Damrey")
typhoon_BST.display()'''


'''typhoon_AVL = AVLTree()
current1 = typhoon_LL.head
while current1 is not None:
    typhoon_AVL.insertRes(current1.name, current1.country)
    current1 = current1.next
typhoon_AVL.display()
typhoon_AVL.search("Nhat")'''