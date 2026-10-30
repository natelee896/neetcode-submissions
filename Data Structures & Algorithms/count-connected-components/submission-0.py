class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True

            for neighbor in graph[node]:
                dfs(neighbor)
        
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        
        return count