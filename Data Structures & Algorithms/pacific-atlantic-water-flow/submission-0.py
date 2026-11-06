class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # need to DFS on both ends 
        m = len(heights)
        n = len(heights[0])

        pac = set()
        atl = set()

        def dfs(r, c, visited, prev):
            if (r, c) in visited or not(0 <= r < m and 0 <= c < n) or heights[r][c] < prev:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            return
        
        # top row for pacific and bottom row for atlantic
        for c in range(n):        
            dfs(0, c, pac, heights[0][c])
            dfs(m - 1, c, atl, heights[m - 1][c])
        
        # left col for pacific and right col for atlantic
        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n - 1, atl, heights[r][n - 1])
        
        result = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pac and (r, c) in atl:
                    result.append((r, c))
        
        return result