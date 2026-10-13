class MinHeap:
    def __init__(self, items=None):
        self.heap = []
        if items:
            self.heap = list(items)
            self.build_heap()

    def check_empty(self):
        return len(self.heap) == 0

    def isEmpty(self):
        return self.check_empty()

    def length(self):
        return len(self.heap)

    def __len__(self):
        return self.length()

    def peek(self):
        if self.isEmpty():
            print("Heap is empty")
            return None
        return self.heap[0]

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def push(self, val):
        self.insert(val)

    def extract_min(self):
        if self.isEmpty():
            print("Heap is empty")
            return None
        min_val = self.heap[0]
        last_val = self.heap.pop()
        if not self.isEmpty():
            self.heap[0] = last_val
            self.heapify_down(0)
        return min_val

    def pop(self):
        return self.extract_min()

    def to_list(self):
        return list(self.heap)

    def display(self):
        if self.isEmpty():
            print("Empty heap")
            return
        for x in self.heap:
            print(x, end=" ")
        print()

    def build_heap(self):
        start = (len(self.heap) // 2) - 1
        for i in range(start, -1, -1):
            self.heapify_down(i)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        size = len(self.heap)
        smallest = index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


class MaxHeap:
    def __init__(self, items=None):
        self.heap = []
        if items:
            self.heap = list(items)
            self.build_heap()

    def check_empty(self):
        return len(self.heap) == 0

    def isEmpty(self):
        return self.check_empty()

    def length(self):
        return len(self.heap)

    def __len__(self):
        return self.length()

    def peek(self):
        if self.isEmpty():
            print("Heap is empty")
            return None
        return self.heap[0]

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def push(self, val):
        self.insert(val)

    def extract_max(self):
        if self.isEmpty():
            print("Heap is empty")
            return None
        max_val = self.heap[0]
        last_val = self.heap.pop()
        if not self.isEmpty():
            self.heap[0] = last_val
            self.heapify_down(0)
        return max_val

    def pop(self):
        return self.extract_max()

    def to_list(self):
        return list(self.heap)

    def display(self):
        if self.isEmpty():
            print("Empty heap")
            return
        for x in self.heap:
            print(x, end=" ")
        print()

    def build_heap(self):
        start = (len(self.heap) // 2) - 1
        for i in range(start, -1, -1):
            self.heapify_down(i)

    def heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def heapify_down(self, index):
        size = len(self.heap)
        largest = index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break


def heapsort(arr, reverse=False):
    res = list(arr)
    n = len(res)
    if n <= 1:
        return res

    def sift_down(start, end, is_max):
        root = start
        while 2 * root + 1 <= end:
            child = 2 * root + 1
            swap = root
            if is_max:
                if res[swap] < res[child]:
                    swap = child
                if child + 1 <= end and res[swap] < res[child + 1]:
                    swap = child + 1
            else:
                if res[swap] > res[child]:
                    swap = child
                if child + 1 <= end and res[swap] > res[child + 1]:
                    swap = child + 1

            if swap == root:
                return
            res[root], res[swap] = res[swap], res[root]
            root = swap

    is_max = not reverse
    for start in range((n - 2) // 2, -1, -1):
        sift_down(start, n - 1, is_max)

    for end in range(n - 1, 0, -1):
        res[0], res[end] = res[end], res[0]
        sift_down(0, end - 1, is_max)

    return res
