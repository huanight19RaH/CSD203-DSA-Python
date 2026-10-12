# CSD203: Data Structures and Algorithms with Python

![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Course](https://img.shields.io/badge/FPT%20University-CSD203-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

Comprehensive implementations of fundamental data structures, algorithms, coursework assignments, and practical examination solutions in Python at FPT University.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Modules and Implementations](#modules-and-implementations)
  - [1. Linear Data Structures](#1-linear-data-structures)
  - [2. Tree Structures](#2-tree-structures)
  - [3. Graph Algorithms](#3-graph-algorithms)
  - [4. Sorting and Searching](#4-sorting-and-searching)
- [Practical Examination Solutions](#practical-examination-solutions)
- [Unit Testing](#unit-testing)
- [Getting Started](#getting-started)
- [Author](#author)
- [License](#license)

---

## Overview

This repository archives verified Python source code and problem solutions for the CSD203 (Data Structures and Algorithms) curriculum. It provides standard implementations of core computer science abstractions alongside solutions to practical examination papers across multiple academic semesters (Summer 2024, Fall 2024, Summer 2025).

---

## Repository Structure

```text
CSD203-DSA-Python/
├── src/
│   ├── linked_list/           # Singly and Doubly Linked Lists
│   ├── tree/                  # Binary Search Tree (BST) and AVL Tree
│   ├── graph/                 # Adjacency matrix, BFS, DFS, Dijkstra, Euler cycle
│   ├── queue_stack/           # FIFO Queue, LIFO Stack, and PriorityQueue
│   └── sorting_searching/     # Bubble, Selection, Insertion, Merge, Quick sort, Binary search
├── assignments/
│   ├── Assignment1a_CSD.py    # List queries, custom PriorityQueue
│   ├── Assignment1b_CSD.py    # Low-level dynamic Array via ctypes
│   └── csd2.py                # Algorithmic exercises
├── practical_exams/
│   ├── pe_fa24/               # Practical Exam Fall 2024 solutions and datasets
│   ├── pe_su24/               # Practical Exam Summer 2024 solutions
│   └── pe_su25/               # Practical Exam Summer 2025 implementations
├── tests/
│   └── test_dsa.py            # Automated unit test suite
├── LICENSE
└── README.md
```

---

## Modules and Implementations

### 1. Linear Data Structures
- **Singly Linked List (`MyList`)**: Append, prepend, insert at index, delete by key, reverse in-place, sort by attribute, convert to list. Includes standard examination routines (`f1`, `f2`, `f3`, `f4`).
- **Doubly Linked List (`DoublyLinkedList`)**: Bidirectional traversal with head and tail pointers, constant-time end insertions, node deletions.
- **Queue and Stack**:
  - `Queue`: FIFO container with constant-time enqueue and dequeue.
  - `Stack`: LIFO container with push, pop, and top inspection.
  - `PriorityQueue`: Node-based priority queue serving higher-priority elements first.

### 2. Tree Structures
- **Binary Search Tree (`BSTree`)**:
  - Insertion, key search, minimum and maximum queries.
  - Traversals: In-Order (LNR), Pre-Order (NLR), Post-Order (LRN), and Breadth-First Search (BFS / Level-Order via Queue).
  - Deletion by copying using in-order predecessor replacement.
  - Tree metric calculations: height, total node count, leaf node count.
- **AVL Tree (`AVLTree`)**:
  - Self-balancing binary search tree maintaining strict balance factor $|BF| \le 1$.
  - Rotations: Left-Left (LL), Right-Right (RR), Left-Right (LR), Right-Left (RL).

### 3. Graph Algorithms
- **Graph (`Graph`)**:
  - Adjacency matrix representation and vertex degree evaluation.
  - Breadth-First Search (BFS) and Depth-First Search (DFS) traversals.
  - Dijkstra's Algorithm for single-source shortest path with full path reconstruction.
  - Eulerian Cycle via Hierholzer's algorithm using Stack.

### 4. Sorting and Searching
- **Sorting**: Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort.
- **Searching**: Binary Search (logarithmic time on sorted arrays), Linear Search.

---

## Practical Examination Solutions

The `practical_exams/` directory contains structured implementations corresponding to FPT University practical exam papers:
- `pe_fa24/`: Practical Exam Fall 2024 (`BST_Tree.py`, `MyList.py`, `PE_Fall24.py`, `typhoon_data.csv`).
- `pe_su24/`: Practical Exam Summer 2024 Paper No. 5 solutions for Linked List, BST, and Graph.
- `pe_su25/`: Practical Exam Summer 2025 question implementations.

---

## Unit Testing

A comprehensive test suite is provided in `tests/test_dsa.py` covering all data structures and algorithms:

```bash
python tests/test_dsa.py
```

All 7 test suites validate operations for linked lists, binary trees, self-balancing AVL trees, graph traversals, shortest paths, queue/stack containers, and sorting algorithms.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher.

### Usage
```bash
# Clone the repository
git clone https://github.com/huanight19RaH/CSD203-DSA-Python.git
cd CSD203-DSA-Python

# Run test suite
python tests/test_dsa.py

# Run an exam solution
python practical_exams/pe_fa24/PE_Fall24.py
```

---

## Author

- **Thai Hung Nguyen (RaH11)**
- Department of Information Technology / Artificial Intelligence, FPT University Da Nang
- GitHub: [@huanight19RaH](https://github.com/huanight19RaH)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
