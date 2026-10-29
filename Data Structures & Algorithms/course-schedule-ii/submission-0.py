class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        zeroDegree = deque()

        for i, degree in enumerate(indegree):
            if degree == 0:
                zeroDegree.append(i) 
        
        courses = []

        while zeroDegree:
            course = zeroDegree.popleft()
            courses.append(course)

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    zeroDegree.append(neighbor)
        
        return courses if len(courses) == numCourses else []