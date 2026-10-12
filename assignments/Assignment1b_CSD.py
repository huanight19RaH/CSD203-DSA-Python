import ctypes

class Planet:
    def __init__(self, name, equatorial_diameter, mass, semi_major_axis, orbital_period):
        self.name = name
        self.equatorial_diameter = equatorial_diameter
        self.mass = mass
        self.semi_major_axis = semi_major_axis
        self.orbital_period = orbital_period
    
    def __str__(self):
        return f"Planet: {self.name}, Mass: {self.mass:.2f}, Equatorial Diameter: {self.equatorial_diameter:.3f}, Semi-Major Axis: {self.semi_major_axis:.2f} (AU), Orbital Period: {self.orbital_period:.2f} (Julian years)"


class Array:
    def __init__(self, size = 1):
        self._n = -1                  
        self._capacity = size
        self._A = self._make_array(size)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k <= self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def _make_array(self, c):
        return (c * ctypes.py_object)()
    
    def _check_increase_size_(self):
        if self._n == self._capacity:
            self._A = self._resize_()
        return
    
    def _resize_(self):
        self._capacity *= 2
        temp_array = self._make_array(self._capacity)
        for i in range(self.length()-1):
            temp_array[i] = self._A[i]
        return temp_array
    
    def length(self):
        return self._n + 1 
    
    def display(self):
        if self.length() == 0:
            print("Empty array")
            print(50 * "-")
        else:
            for i in range(self.length()):
                print(self._A[i])
            print(50 * "-")
        
    def insert(self, value, index = None):
        self._n += 1
        self._check_increase_size_()
        if index == None:
            self._A[self._n] = value
            return
        for i in range(self._n, index, -1):
            self._A[i] = self._A[i-1]
        self._A[index] = value
        return 
    
    def remove(self, index = None):
        if index == None:
            self._A[self._n] = None
            self._n -=1
            return
        for i in range(index, self.length()-1):
            self._A[i] = self._A[i+1]
        self._n -=1
        return 
    
    def clear(self):
        for i in range(self.length()-1, -1, -1):
            self.remove(i) 
        self._capacity = 1
        return
    
solar_system_array = Array(10)

solar_system_array.insert(Planet("Mercury", 0.383, 0.06, 0.39, 0.24))
solar_system_array.insert(Planet("Venus", 0.949, 0.81, 0.72, 0.62))
solar_system_array.insert(Planet("Earth", 1.000, 1.00, 1.00, 1.00))
solar_system_array.insert(Planet("Mars", 0.532, 0.11, 1.52, 1.88))
solar_system_array.insert(Planet("Jupiter", 11.209, 317.83, 5.20, 11.86))
solar_system_array.insert(Planet("Saturn", 9.449, 95.16, 9.54, 29.45),)
solar_system_array.insert(Planet("Uranus", 4.007, 14.54, 19.19, 84.02))
solar_system_array.insert(Planet("Neptune", 3.883, 17.15, 30.07, 164.79))
    
print("Solar System Planets Ordered by Mass:\n" + 50 * "-")
solar_system_array.display()
print(f"Number of planets: {solar_system_array.length()}\n" + 50 * "-")

solar_system_array.remove()
solar_system_array.display()