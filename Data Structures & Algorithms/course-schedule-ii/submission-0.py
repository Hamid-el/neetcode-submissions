class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Adjacency List
        graph = [[] for _ in range(numCourses)] # numCourses = anzahl an nodes
        indegree = [0] * numCourses # anzahl an eingehenden kanten = wie viele Voraussetzungen ein Kurs noch hat

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # all courses without prereq
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        res = []

        # BFS
        while queue:
            course = queue.popleft()
            res.append(course)

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        if len(res) != numCourses:
            return []
        return res
