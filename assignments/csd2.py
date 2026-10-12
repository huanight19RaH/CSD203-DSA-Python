class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def check_empty(self):
        return self.head == None
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = " ")
            current = current.next
    
    def insertLast(self, val):
        newNode = Node(val)
        if self.check_empty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            
    def insertFirst(self, val):
        newNode = Node(val)
        if self.check_empty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def removeFirst(self):
        if self.check_empty():
            print("Empty")
        else:
            self.head = self.head.next
    
    def removeLast(self):
        if self.check_empty():
            print("Empty")
        else:
            if self.head is self.tail: #Truong hop chi co 1 node, khong co .next đc
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current
                
    def removeValue(self, val):
        if self.check_empty():
            print("Empty")
        elif val == self.head.data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next.data != val:
                current = current.next
            current.next = current.next.next
                    
                
            
list1 = SinglyLinkedList()
list1.insertLast(1)
list1.insertLast(3)
list1.insertLast(5)
list1.insertLast(7)
list1.insertFirst(9)
list1.removeFirst()
list1.removeLast()
list1.removeValue(1)
list1.display()