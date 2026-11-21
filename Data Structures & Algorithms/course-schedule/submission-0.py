class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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

        completed = 0

        # BFS
        while queue:
            course = queue.popleft()
            completed += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed == numCourses
