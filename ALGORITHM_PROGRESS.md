# CSD203: Bảng Theo Dõi Tiến Trình & Kế Hoạch Triển Khai Thuật Toán (DSA Roadmap)

Bảng phân rã tiến trình toàn diện các cấu trúc dữ liệu và giải thuật trong chương trình **CSD203 (Data Structures and Algorithms with Python - ĐH FPT)**.

---

## 📌 Quy Ước Ký Hiệu
- `[x]` **Hoàn thành:** Đã viết mã nguồn chuẩn, có unit test tự động pass 100% và đã push lên GitHub.
- `[-]` **Đang thực hiện:** Đang trong phiên làm việc hoặc đang kiểm thử.
- `[ ]` **Chưa thực hiện:** Đã lên kế hoạch chi tiết, sẵn sàng cho các phiên làm việc tiếp theo.

---

## 📊 Bảng Tiến Trình Chi Tiết Theo Phân Hệ

### 1. Linear Data Structures (Cấu trúc tuyến tính - Ch5, Ch6, Ch7)
- [x] **Singly Linked List (`MyList`)**: Append, Prepend, Insert At, Delete, Reverse, Sort by attribute, f1-f4 PE routines (`src/linked_list/singly_linked_list.py`)
- [x] **Doubly Linked List (`DoublyLinkedList`)**: Bidirectional next/prev, insertFirst/Last, removeFirst/Last, display (`src/linked_list/doubly_linked_list.py`)
- [x] **FIFO Queue (`Queue`)**: Enqueue, Dequeue, Peek, isEmpty (`src/queue_stack/queue.py`)
- [x] **LIFO Stack (`Stack`)**: Push, Pop, Top, isEmpty (`src/queue_stack/stack.py`)
- [x] **Priority Queue (`PriorityQueue`)**: Node-based priority queue (`src/queue_stack/queue.py`)
- [ ] **Circular Linked List (`CircularLinkedList`)**: Danh sách liên kết vòng (Kế hoạch Session 3)

### 2. Tree Structures (Cấu trúc cây - Ch8, Ch11)
- [x] **Binary Search Tree (`BSTree`)**: Insert, Search, Min/Max, Traversals (In-order, Pre-order, Post-order, Breadth-first / Level-order), Delete by copying, Height, Count nodes (`src/tree/binary_search_tree.py`)
- [x] **AVL Tree (`AVLTree`)**: Self-balancing BST, 4 phép quay LL, RR, LR, RL, cập nhật chiều cao và hệ số cân bằng (`src/tree/avl_tree.py`)
- [ ] **Splay Tree**: Cây tự cân bằng theo truy cập gần nhất (Splaying) (Kế hoạch Session 4)
- [ ] **Red-Black Tree**: Cây đỏ đen đảm bảo độ lệch chiều cao $\le 2$ (Kế hoạch Session 4)

### 3. Heap & Priority Queue (Ch9)
- [x] **Binary MinHeap (`MinHeap`)**: Insert/Push, Extract-Min/Pop, Peek, Heapify-up/down, Floyd's $O(n)$ `build_heap` (`src/heap/heap.py`)
- [x] **Binary MaxHeap (`MaxHeap`)**: Insert/Push, Extract-Max/Pop, Peek, Heapify-up/down, Floyd's $O(n)$ `build_heap` (`src/heap/heap.py`)
- [x] **HeapSort (`heapsort`)**: Thuật toán sắp xếp vun đống in-place $O(n \log n)$, $O(1)$ auxiliary space, hỗ trợ ascending & descending (`src/heap/heap.py`)

### 4. Sorting & Searching (Sắp xếp & Tìm kiếm - Ch12)
- [x] **Bubble Sort**: Sắp xếp nổi bọt $O(n^2)$ (`src/sorting_searching/sorting_searching.py`)
- [x] **Selection Sort**: Sắp xếp chọn $O(n^2)$ (`src/sorting_searching/sorting_searching.py`)
- [x] **Insertion Sort**: Sắp xếp chèn $O(n^2)$ (`src/sorting_searching/sorting_searching.py`)
- [x] **Merge Sort**: Sắp xếp trộn chia để trị $O(n \log n)$ (`src/sorting_searching/sorting_searching.py`)
- [x] **Quick Sort**: Sắp xếp nhanh phân hoạch Lomuto/Hoare $O(n \log n)$ (`src/sorting_searching/sorting_searching.py`)
- [x] **Binary Search**: Tìm kiếm nhị phân $O(\log n)$ trên mảng đã sắp xếp (`src/sorting_searching/sorting_searching.py`)
- [ ] **Counting Sort**: Sắp xếp đếm tuyến tính $O(n + k)$ (Kế hoạch Session 3)
- [ ] **Radix Sort**: Sắp xếp cơ số tuyến tính theo chữ số (Kế hoạch Session 3)

### 5. Graph Algorithms (Thuật toán đồ thị - Ch14)
- [x] **Graph Adjacency Matrix**: Khởi tạo, ma trận kề, bậc đỉnh `degree(v)` (`src/graph/graph_algorithms.py`)
- [x] **Breadth-First Search (`bfs`)**: Duyệt theo chiều rộng dùng Queue (`src/graph/graph_algorithms.py`)
- [x] **Depth-First Search (`dfs`)**: Duyệt theo chiều sâu dùng đệ quy (`src/graph/graph_algorithms.py`)
- [x] **Dijkstra Shortest Path (`dijkstra`)**: Đường đi ngắn nhất nguồn đơn, tái dựng đường đi và khoảng cách (`src/graph/graph_algorithms.py`)
- [x] **Eulerian Cycle (`euler_cycle`)**: Chu trình Euler qua thuật toán Hierholzer dùng Stack (`src/graph/graph_algorithms.py`)
- [x] **Disjoint Set Union (`DisjointSet`)**: Cấu trúc tập hợp rời rạc với Path Compression & Union by Rank (`src/graph/disjoint_set.py`)
- [x] **Kruskal's MST Algorithm (`kruskal_mst`)**: Cây khung nhỏ nhất qua DSU và sắp xếp cạnh (`src/graph/graph_algorithms.py`)
- [x] **Prim's MST Algorithm (`prim_mst`)**: Cây khung nhỏ nhất từ đỉnh xuất phát qua lát cắt vết thăm (`src/graph/graph_algorithms.py`)
- [x] **Topological Sort (`topological_sort`)**: Sắp xếp topo cho đồ thị có hướng không chu trình (DAG) bằng Kahn's Algorithm & phát hiện chu trình (`src/graph/graph_algorithms.py`)

### 6. Hash Tables & Maps (Bảng băm - Ch10)
- [ ] **Separate Chaining Hash Table (`ChainingHashTable`)**: Bảng băm giải quyết đụng độ bằng danh sách móc nối (Kế hoạch Session 2)
- [ ] **Open Addressing Hash Table (`LinearProbingHashTable`)**: Bảng băm với dò tuyến tính, tự động resize khi load factor $\ge 0.75$ (Kế hoạch Session 2)

### 7. String Processing & Text Algorithms (Xử lý chuỗi - Ch13)
- [ ] **Trie / Prefix Tree (`Trie`, `TrieNode`)**: Chèn từ, tìm kiếm từ, tiền tố `starts_with`, gợi ý tự động (Kế hoạch Session 2)
- [ ] **KMP Pattern Matching (`kmp_search`)**: So khớp chuỗi Knuth-Morris-Pratt qua mảng tiền tố LPS $O(n + m)$ (Kế hoạch Session 2)

### 8. Dynamic Programming & Greedy (Quy hoạch động & Tham lam - Ch13)
- [ ] **0/1 Knapsack Problem**: Bài toán cái ba lô dùng bảng phương án quy hoạch động (Kế hoạch Session 5)
- [ ] **Longest Common Subsequence (LCS)**: Chuỗi con chung dài nhất (Kế hoạch Session 5)
- [ ] **Huffman Coding**: Nén dữ liệu dùng cây nhị phân tham lam và Priority Queue (Kế hoạch Session 5)

---

## 🗓️ Lộ Trình Triển Khai Từng Buổi (Session Roadmap)

| Buổi (Session) | Mục Tiêu Triển Khai | Trạng Thái |
| :--- | :--- | :---: |
| **Session 1 (Đã hoàn thành)** | **Graph Nâng Cao:** `DisjointSet` (Union-Find), `Kruskal MST`, `Prim MST`, `Topological Sort` (DAG) | **HOÀN THÀNH** |
| **Session 2 (Kế tiếp)** | **Hash Tables & String:** `ChainingHashTable`, `LinearProbingHashTable`, `Trie`, `KMP Algorithm` | Chờ triển khai |
| **Session 3** | **Linear & Sorting Mở Rộng:** `CircularLinkedList`, `Counting Sort`, `Radix Sort` | Chờ triển khai |
| **Session 4** | **Advanced Trees:** `Splay Tree`, `Red-Black Tree` | Chờ triển khai |
| **Session 5** | **Dynamic Programming & Greedy:** `0/1 Knapsack`, `LCS`, `Huffman Coding` | Chờ triển khai |

---

## 🛠️ Hướng Dẫn Tiếp Tục Cho Các Buổi Sau
Khi mở phiên làm việc mới:
1. Đọc file này (`ALGORITHM_PROGRESS.md`) để xác định ngay Session và các mục `[ ]` tiếp theo cần làm.
2. Viết mã nguồn tương thích với phong cách CSD cá nhân tại thư mục `src/`.
3. Bổ sung test suite vào `tests/test_dsa.py` và chạy `python3 tests/test_dsa.py`.
4. Đổi trạng thái từ `[ ]` sang `[x]` trong file này và cập nhật `README.md`.
5. Thực hiện commit với `--author="RaH11 <hungnguyen.190206@gmail.com>"` và push lên `origin/main`.
