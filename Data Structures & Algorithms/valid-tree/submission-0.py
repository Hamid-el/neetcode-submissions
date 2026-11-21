class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = list(range(n)) # [1,2...,n-1], later is at i its parent from beginning
        size = [1] * n # size[i] stores #Nodes in component, deren Root i ist.

        def find_root(node):
            if parent[node] != node:
                parent[node] = find_root(parent[node])

            return parent[node]

        def union(node_a, node_b):
            root_a = find_root(node_a)
            root_b = find_root(node_b)

            if root_a == root_b: # has cycle
                return False

            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True

        for node_a, node_b in edges:
            if not union(node_a, node_b):
                return False

        return True
