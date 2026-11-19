class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        result = 0
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        visited = set()

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return 
            grid[r][c] = '0'
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] =='1':
                    result += 1
                    dfs(r, c)
        
        return result