class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges) + 1)]

        def bfs(start, target):
            queue = deque([start])
            visited = {start} # set with start in it

            while queue:
                node = queue.popleft()

                if node == target:
                    return True

                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return False

        for node_a, node_b in edges:
            if bfs(node_a, node_b):
                return [node_a, node_b]

            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        return []
