"""
CSD203 - Graph Algorithms Implementation
Supports Adjacency Matrix representation, BFS, DFS,
Dijkstra's Shortest Path, Eulerian Cycle (Fleury/Hierholzer), and Prim's MST.
"""

import math
from collections import deque

class Graph:
    def __init__(self, matrix=None):
        """Initialize graph with adjacency matrix."""
        self.a = matrix if matrix is not None else []

    def set_matrix(self, matrix):
        self.a = matrix

    def num_vertices(self):
        return len(self.a)

    def degree(self, v):
        """Calculate degree of vertex v."""
        return sum(1 for j in range(len(self.a)) if self.a[v][j] != 0)

    # --- Traversals ---

    def bfs(self, start=0):
        """Breadth-First Search traversal."""
        visited = [False] * len(self.a)
        result = []
        queue = deque([start])
        visited[start] = True

        while queue:
            u = queue.popleft()
            result.append(chr(u + 65))

            for v in range(len(self.a)):
                if self.a[u][v] != 0 and not visited[v]:
                    visited[v] = True
                    queue.append(v)
        return result

    def dfs(self, start=0):
        """Depth-First Search traversal."""
        visited = [False] * len(self.a)
        result = []

        def _dfs_rec(u):
            visited[u] = True
            result.append(chr(u + 65))
            for v in range(len(self.a)):
                if self.a[u][v] != 0 and not visited[v]:
                    _dfs_rec(v)

        _dfs_rec(start)
        return result

    # --- Dijkstra Shortest Path ---

    def dijkstra(self, start, end):
        """
        Dijkstra's Algorithm finding the shortest path from start to end.
        Handles both integer indices and character inputs ('A', 'B', ...).
        Returns (path_str, distance_str, total_cost).
        """
        # Convert char to int if needed
        s = ord(start.upper()) - 65 if isinstance(start, str) else start
        e = ord(end.upper()) - 65 if isinstance(end, str) else end

        n = len(self.a)
        dist = [math.inf] * n
        parent = [-1] * n
        visited = [False] * n

        dist[s] = 0

        for _ in range(n):
            # Pick min distance unvisited vertex
            u = -1
            min_d = math.inf
            for i in range(n):
                if not visited[i] and dist[i] < min_d:
                    min_d = dist[i]
                    u = i

            if u == -1 or u == e:
                break
            visited[u] = True

            for v in range(n):
                if self.a[u][v] != 0 and not visited[v]:
                    new_dist = dist[u] + self.a[u][v]
                    if new_dist < dist[v]:
                        dist[v] = new_dist
                        parent[v] = u

        # Reconstruct path
        if dist[e] == math.inf:
            return ("No path", "Infinity", math.inf)

        path = []
        curr = e
        while curr != -1:
            path.append(curr)
            curr = parent[curr]
        path.reverse()

        path_str = "-".join([chr(v + 65) for v in path])
        dist_str = "-".join([f"{chr(v + 65)}({dist[v]})" for v in path])
        return (path_str, dist_str, dist[e])

    # --- Eulerian Cycle ---

    def euler_cycle(self, start=0):
        """
        Hierholzer's Algorithm using Stack to find Eulerian Cycle.
        """
        s = ord(start.upper()) - 65 if isinstance(start, str) else start
        n = len(self.a)
        # Deep copy adjacency matrix to mutate during traversal
        adj = [row[:] for row in self.a]

        stack = [s]
        cycle = []

        while stack:
            u = stack[-1]
            # Check if u has remaining unvisited edges
            has_edge = False
            for v in range(n):
                if adj[u][v] != 0:
                    stack.append(v)
                    adj[u][v] = 0
                    adj[v][u] = 0
                    has_edge = True
                    break
            if not has_edge:
                cycle.append(chr(stack.pop() + 65))

        cycle.reverse()
        return " ".join(cycle)
