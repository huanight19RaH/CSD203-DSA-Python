import math
from Employee import *
from Node import *
class MyList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head ==None
    def traverse(self):
        pt = self.head
        while pt.next:
            print(pt.data, end = " ")
            pt = pt.next
        print(pt.data)        
    def clear(self):
        self.head = None    
#Q1-1
    def f1(self, name="", age="", salary=-1):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        if name.startswith("Z") or age < 15 or salary <=0:
            return
        else:
            n = Node(Employee(name,age,salary))
    #         node = Node(name, price)
            if self.isEmpty():
                self.head = n
                self.tail = n
            else:
                n.next = self.head #cho addfirst keets noi va dua len head(dau tien)
                self.head = n        
    # end def
#Q1-2          
    def f2(self, A):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        if self.head == None:
            self.head = A
            return
        cur = self.head
        while cur:
            if cur.data.Age % 2 == 0:#sửa điều kiện theo yêu cầu đề bài
                A.next = cur.next
                cur.next = A
                break
            cur = cur.next 
    # end def
#Q1-3
    def f3(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 3 ========
        if self.head is None:
            return
        # Check if the first node's age is a square number
        if self.head.data.Age % 2 == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current is not None:
            if current.data.Age % 2 == 0: #sửa điều kiện theo yêu cầu đề bài
                prev.next = current.next
                return
            prev = current
            current = current.next
    #end def
# Q1-4
    def count(self):
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next 
        return count
    
    def f4(self):
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 4 ========
        totalNode = self.count()
        
        lst2 = []
        cur = self.head
        for i in range(totalNode):
            if i % 2 == 1:
                lst2.append((cur.data.Name, cur.data.Salary))
            cur = cur.next
        
        lst2 = sorted(lst2, key = lambda x: x[1], reverse=True)
        j = 0
        cur = self.head
        for i in range(totalNode):
            if i % 2 == 1:
                cur.data.Name = lst2[j][0]
                cur.data.Salary = lst2[j][1]
                j += 1
            cur = cur.next
    #end def

    