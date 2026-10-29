class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        zeroDegree = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                zeroDegree.append(i)
        
        completed = 0

        while zeroDegree:
            course = zeroDegree.popleft()
            completed += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    zeroDegree.append(neighbor)
        
        return completed == numCourses