import unittest
import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from linked_list.singly_linked_list import MyList, Product
from linked_list.doubly_linked_list import DoublyLinkedList
from tree.binary_search_tree import BSTree
from tree.avl_tree import AVLTree
from graph.graph_algorithms import Graph
from graph.disjoint_set import DisjointSet, UnionFind
from queue_stack.queue import Queue, PriorityQueue
from queue_stack.stack import Stack
from sorting_searching.sorting_searching import (
    bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, binary_search
)
from heap.heap import MinHeap, MaxHeap, heapsort

class TestDSA(unittest.TestCase):
    def test_singly_linked_list(self):
        ll = MyList()
        ll.append(10)
        ll.append(20)
        ll.prepend(5)
        self.assertEqual(ll.to_list(), [5, 10, 20])
        ll.reverse()
        self.assertEqual(ll.to_list(), [20, 10, 5])

        # Test FPT exam functions
        p_list = MyList()
        p_list.f1(2, "Apple", 50)
        p_list.f1(4, "Banana", 80)
        p_list.f1(1, "Orange", 30)
        self.assertEqual(len(p_list), 3)

    def test_doubly_linked_list(self):
        dll = DoublyLinkedList()
        dll.append(1)
        dll.append(2)
        dll.prepend(0)
        self.assertEqual(len(dll), 3)
        dll.delete(1)
        self.assertEqual(len(dll), 2)

    def test_bst(self):
        bst = BSTree()
        for x in [50, 30, 70, 20, 40, 60, 80]:
            bst.insert(x)
        self.assertEqual(bst.in_order(), [20, 30, 40, 50, 60, 70, 80])
        self.assertEqual(bst.pre_order(), [50, 30, 20, 40, 70, 60, 80])
        self.assertEqual(bst.breadth_first(), [50, 30, 70, 20, 40, 60, 80])
        self.assertEqual(bst.height(), 3)
        self.assertEqual(bst.count_nodes(), 7)
        self.assertIsNotNone(bst.search(40))
        self.assertIsNone(bst.search(100))

        # Test delete by copying
        bst.delete_by_copying(30)
        self.assertEqual(bst.in_order(), [20, 40, 50, 60, 70, 80])

    def test_avl_tree(self):
        avl = AVLTree()
        # Inserting sequentially would cause linear skew in regular BST
        for x in [10, 20, 30, 40, 50, 25]:
            avl.insert(x)
        self.assertEqual(avl.in_order(), [10, 20, 25, 30, 40, 50])
        # AVL height should remain logarithmic (<= 3 or 4)
        self.assertLessEqual(avl.get_height(avl.root), 4)

    def test_disjoint_set(self):
        dsu = DisjointSet(n=5)
        self.assertEqual(dsu.count_sets(), 5)
        self.assertTrue(dsu.union(0, 1))
        self.assertTrue(dsu.union(1, 2))
        self.assertFalse(dsu.union(0, 2))  # Already in same set (cycle)
        self.assertTrue(dsu.connected(0, 2))
        self.assertFalse(dsu.connected(0, 3))
        self.assertEqual(dsu.count_sets(), 3)

        # Test character elements
        char_dsu = DisjointSet(['A', 'B', 'C', 'D'])
        self.assertTrue(char_dsu.union('A', 'B'))
        self.assertTrue(char_dsu.connected('A', 'B'))
        self.assertFalse(char_dsu.connected('A', 'C'))

    def test_graph(self):
        # 5-node graph with weighted adjacency matrix
        # 0=A, 1=B, 2=C, 3=D, 4=E
        matrix = [
            [0, 2, 4, 0, 0],
            [2, 0, 1, 7, 0],
            [4, 1, 0, 0, 3],
            [0, 7, 0, 0, 1],
            [0, 0, 3, 1, 0]
        ]
        g = Graph(matrix)
        self.assertEqual(g.bfs(0), ['A', 'B', 'C', 'D', 'E'])
        path_str, dist_str, cost = g.dijkstra('A', 'D')
        # Shortest path A -> B -> C -> E -> D: 2 + 1 + 3 + 1 = 7
        self.assertEqual(cost, 7)
        self.assertEqual(path_str, "A-B-C-E-D")

        # Test Prim's MST
        prim_edges, prim_weight, prim_str = g.prim_mst('A')
        self.assertEqual(prim_weight, 7)
        self.assertEqual(len(prim_edges), 4)

        # Test Kruskal's MST
        kruskal_edges, kruskal_weight, kruskal_str = g.kruskal_mst()
        self.assertEqual(kruskal_weight, 7)
        self.assertEqual(len(kruskal_edges), 4)

        # Test Topological Sort on DAG
        dag_matrix = [
            [0, 1, 1, 0],  # A -> B, C
            [0, 0, 0, 1],  # B -> D
            [0, 0, 0, 1],  # C -> D
            [0, 0, 0, 0]   # D has no outgoing
        ]
        dag = Graph(dag_matrix)
        order, order_str, has_cycle = dag.topological_sort()
        self.assertFalse(has_cycle)
        self.assertEqual(order[0], 'A')
        self.assertEqual(order[-1], 'D')

        # Test Topological Sort Cycle Detection
        cyclic_matrix = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 0]
        ]
        cyclic_graph = Graph(cyclic_matrix)
        order_c, order_str_c, has_cycle_c = cyclic_graph.topological_sort()
        self.assertTrue(has_cycle_c)
        self.assertIsNone(order_c)

    def test_queue_and_stack(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.peek(), 2)

        pq = PriorityQueue()
        pq.enqueue("Low", 1)
        pq.enqueue("High", 10)
        pq.enqueue("Mid", 5)
        self.assertEqual(pq.dequeue(), "High")
        self.assertEqual(pq.dequeue(), "Mid")

        st = Stack()
        st.push("first")
        st.push("second")
        self.assertEqual(st.pop(), "second")

    def test_sorting_and_searching(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bubble_sort(arr), expected)
        self.assertEqual(selection_sort(arr), expected)
        self.assertEqual(insertion_sort(arr), expected)
        self.assertEqual(merge_sort(arr), expected)
        self.assertEqual(quick_sort(arr), expected)

        sorted_arr = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(binary_search(sorted_arr, 25), 3)
        self.assertEqual(binary_search(sorted_arr, 999), -1)

    def test_heap(self):
        # MinHeap insertion and extraction
        min_h = MinHeap()
        for v in [50, 30, 20, 40, 10]:
            min_h.insert(v)
        self.assertEqual(len(min_h), 5)
        self.assertEqual(min_h.peek(), 10)
        extracted = [min_h.extract_min() for _ in range(5)]
        self.assertEqual(extracted, [10, 20, 30, 40, 50])

        # MinHeap O(n) build from list
        built_min = MinHeap([35, 12, 45, 2, 8, 19])
        self.assertEqual(built_min.extract_min(), 2)

        # MaxHeap insertion and extraction
        max_h = MaxHeap()
        for v in [10, 40, 20, 50, 30]:
            max_h.insert(v)
        self.assertEqual(max_h.peek(), 50)
        max_extracted = [max_h.extract_max() for _ in range(5)]
        self.assertEqual(max_extracted, [50, 40, 30, 20, 10])

        # Heapsort ascending & descending
        arr = [64, 34, 25, 12, 22, 11, 90]
        self.assertEqual(heapsort(arr), [11, 12, 22, 25, 34, 64, 90])
        self.assertEqual(heapsort(arr, reverse=True), [90, 64, 34, 25, 22, 12, 11])

if __name__ == '__main__':
    unittest.main()
