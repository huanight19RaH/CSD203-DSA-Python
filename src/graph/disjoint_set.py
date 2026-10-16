class DisjointSet:
    """
    Disjoint Set Union (DSU) / Union-Find data structure.
    Implements Path Compression and Union by Rank for near constant amortized time O(alpha(n)).
    Supports both integer indices and character/string elements.
    """

    def __init__(self, elements=None, n=None):
        self.parent = {}
        self.rank = {}
        if n is not None:
            for i in range(n):
                self.parent[i] = i
                self.rank[i] = 0
        elif elements is not None:
            for x in elements:
                self.parent[x] = x
                self.rank[x] = 0

    def make_set(self, x):
        """Add a single isolated element if not present."""
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, i):
        """Find representative root of set containing i with path compression."""
        if i not in self.parent:
            self.make_set(i)
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        """
        Merge sets containing i and j using union by rank.
        Returns True if merged, False if i and j are already in the same set (cycle detected).
        """
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False

        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
        return True

    def connected(self, i, j):
        """Check if i and j belong to the same connected component."""
        return self.find(i) == self.find(j)

    def is_connected(self, i, j):
        return self.connected(i, j)

    def count_sets(self):
        """Return the number of disjoint sets."""
        roots = set(self.find(x) for x in self.parent)
        return len(roots)

    def length(self):
        return len(self.parent)

    def __len__(self):
        return self.length()

    def get_components(self):
        """Return dictionary mapping representative root to members."""
        components = {}
        for x in self.parent:
            root = self.find(x)
            if root not in components:
                components[root] = []
            components[root].append(x)
        return components


# Alias
UnionFind = DisjointSet
