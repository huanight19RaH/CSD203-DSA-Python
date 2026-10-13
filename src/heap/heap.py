"""
CSD203 - Binary Heap and HeapSort Implementation
Provides MinHeap, MaxHeap, and in-place HeapSort algorithms.
"""

from typing import List, Any, Optional


class MinHeap:
    """
    Array-based Binary Min-Heap implementation.
    The parent is always smaller than or equal to its children.
    """

    def __init__(self, items: Optional[List[Any]] = None):
        self._heap: List[Any] = []
        if items:
            self._heap = list(items)
            self._build_heap()

    def __len__(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def peek(self) -> Any:
        """Return the minimum element without removing it. O(1) time."""
        if self.is_empty():
            raise IndexError("Peek from an empty MinHeap.")
        return self._heap[0]

    def insert(self, val: Any) -> None:
        """Insert a new element into the heap. O(log n) time."""
        self._heap.append(val)
        self._heapify_up(len(self._heap) - 1)

    def push(self, val: Any) -> None:
        """Alias for insert."""
        self.insert(val)

    def extract_min(self) -> Any:
        """Remove and return the minimum element. O(log n) time."""
        if self.is_empty():
            raise IndexError("Extract from an empty MinHeap.")
        min_val = self._heap[0]
        last_val = self._heap.pop()
        if not self.is_empty():
            self._heap[0] = last_val
            self._heapify_down(0)
        return min_val

    def pop(self) -> Any:
        """Alias for extract_min."""
        return self.extract_min()

    def to_list(self) -> List[Any]:
        """Return a copy of the underlying array representation."""
        return list(self._heap)

    def _build_heap(self) -> None:
        """Floyd's heap construction algorithm running in O(n) time."""
        start_idx = (len(self._heap) // 2) - 1
        for i in range(start_idx, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self._heap[index] < self._heap[parent]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index: int) -> None:
        size = len(self._heap)
        smallest = index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self._heap[left] < self._heap[smallest]:
                smallest = left
            if right < size and self._heap[right] < self._heap[smallest]:
                smallest = right

            if smallest != index:
                self._heap[index], self._heap[smallest] = self._heap[smallest], self._heap[index]
                index = smallest
            else:
                break


class MaxHeap:
    """
    Array-based Binary Max-Heap implementation.
    The parent is always greater than or equal to its children.
    """

    def __init__(self, items: Optional[List[Any]] = None):
        self._heap: List[Any] = []
        if items:
            self._heap = list(items)
            self._build_heap()

    def __len__(self) -> int:
        return len(self._heap)

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def peek(self) -> Any:
        """Return the maximum element without removing it. O(1) time."""
        if self.is_empty():
            raise IndexError("Peek from an empty MaxHeap.")
        return self._heap[0]

    def insert(self, val: Any) -> None:
        """Insert a new element into the heap. O(log n) time."""
        self._heap.append(val)
        self._heapify_up(len(self._heap) - 1)

    def push(self, val: Any) -> None:
        """Alias for insert."""
        self.insert(val)

    def extract_max(self) -> Any:
        """Remove and return the maximum element. O(log n) time."""
        if self.is_empty():
            raise IndexError("Extract from an empty MaxHeap.")
        max_val = self._heap[0]
        last_val = self._heap.pop()
        if not self.is_empty():
            self._heap[0] = last_val
            self._heapify_down(0)
        return max_val

    def pop(self) -> Any:
        """Alias for extract_max."""
        return self.extract_max()

    def to_list(self) -> List[Any]:
        """Return a copy of the underlying array representation."""
        return list(self._heap)

    def _build_heap(self) -> None:
        """Floyd's heap construction algorithm running in O(n) time."""
        start_idx = (len(self._heap) // 2) - 1
        for i in range(start_idx, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index: int) -> None:
        parent = (index - 1) // 2
        while index > 0 and self._heap[index] > self._heap[parent]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index: int) -> None:
        size = len(self._heap)
        largest = index
        while True:
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self._heap[left] > self._heap[largest]:
                largest = left
            if right < size and self._heap[right] > self._heap[largest]:
                largest = right

            if largest != index:
                self._heap[index], self._heap[largest] = self._heap[largest], self._heap[index]
                index = largest
            else:
                break


def heapsort(arr: List[Any], reverse: bool = False) -> List[Any]:
    """
    In-place Heap Sort algorithm.
    Time Complexity: O(n log n)
    Space Complexity: O(1) auxiliary space (modifies and returns a copy).
    """
    res = list(arr)
    n = len(res)
    if n <= 1:
        return res

    def _sift_down(start: int, end: int, is_max: bool):
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

    is_max_heap = not reverse

    # Phase 1: Build heap O(n)
    for start in range((n - 2) // 2, -1, -1):
        _sift_down(start, n - 1, is_max_heap)

    # Phase 2: Extract elements one by one O(n log n)
    for end in range(n - 1, 0, -1):
        res[0], res[end] = res[end], res[0]
        _sift_down(0, end - 1, is_max_heap)

    return res
