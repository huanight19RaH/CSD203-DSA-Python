class Planet:
    def __init__(self, name, equatorial_diameter, mass, semi_major_axis, orbital_period):
        self.name = name
        self.equatorial_diameter = equatorial_diameter
        self.mass = mass
        self.semi_major_axis = semi_major_axis
        self.orbital_period = orbital_period
    
    def __str__(self):
        return f"Planet: {self.name}, Mass: {self.mass:.2f}, Equatorial Diameter: {self.equatorial_diameter:.3f}, Semi-Major Axis: {self.semi_major_axis:.2f} (AU), Orbital Period: {self.orbital_period:.2f} (Julian years)"

class Node:
    def __init__(self, data, prior):
        self.data = data
        self.prior = prior
        self.next = None
        
class PriorityQueue:
    def __init__(self):
        self.head = self.tail = None
    
    def isEmpty(self):
        return self.head is None
    
    def len(self):
        if self.isEmpty():
            return 0
        else:
            current = self.head
            length = 0
            while current is not None:
                length += 1
                current = current.next
            return length
        
    def display(self):
        if self.isEmpty():
            print("Empty Queue")
            print(50 * "-")
        else:
            current = self.head
            while current is not None:
                print(current.data)
                current = current.next
            print(50 * "-")
    
    def enqueue(self, val, prior=0):
        newNode = Node(val, prior)
        if self.isEmpty():
            self.head = self.tail = newNode
        elif prior >= self.head.prior: 
            newNode.next = self.head
            self.head = newNode
        elif prior <= self.tail.prior:
            self.tail.next = newNode
            self.tail = newNode
        else:
            current = self.head
            currentNext = current.next
            while currentNext is not None and currentNext.prior > prior:
                current = currentNext
                currentNext = currentNext.next
            newNode.next = current.next
            current.next = newNode
    
    def deleteMax(self):
        if self.isEmpty():
            print("Empty Queue")
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp
        
    def deleteMin(self):
        if self.isEmpty():
            print("Empty Queue")
            return None
        elif self.head == self.tail:
            self.head = None
            return self.head
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            temp = self.tail
            self.tail = current
            current.next = None
            return temp
    
    def searchMax(self):
        if self.isEmpty():
            print("Empty Queue")
            return None
        else:
            return self.head
    
    def searchMin(self):
        if self.isEmpty():
            print("Empty Queue")
            return None
        else:
            return self.tail
    
    

solar_system_queue = PriorityQueue()

solar_system_queue.enqueue(Planet("Mercury", 0.383, 0.06, 0.39, 0.24), 0.06)
solar_system_queue.enqueue(Planet("Venus", 0.949, 0.81, 0.72, 0.62), 0.81)
solar_system_queue.enqueue(Planet("Earth", 1.000, 1.00, 1.00, 1.00), 1.00)
solar_system_queue.enqueue(Planet("Mars", 0.532, 0.11, 1.52, 1.88), 0.11)
solar_system_queue.enqueue(Planet("Jupiter", 11.209, 317.83, 5.20, 11.86), 317.83)
solar_system_queue.enqueue(Planet("Saturn", 9.449, 95.16, 9.54, 29.45), 95.16)
solar_system_queue.enqueue(Planet("Uranus", 4.007, 14.54, 19.19, 84.02), 14.54)
solar_system_queue.enqueue(Planet("Neptune", 3.883, 17.15, 30.07, 164.79), 17.15)
    
print("Solar System Planets Ordered by Mass:\n" + 50 * "-")
solar_system_queue.display()
print(f"Number of planets: {solar_system_queue.len()}\n" + 50 * "-")
print(f"The planet deleted: {solar_system_queue.deleteMin().data}\n" + 50 * "-")
solar_system_queue.display()
print(f"The planet have the max mass: {solar_system_queue.searchMax().data}")
print(f"The planet have the min mass: {solar_system_queue.searchMin().data}")