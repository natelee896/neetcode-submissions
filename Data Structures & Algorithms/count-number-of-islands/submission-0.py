class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        count = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0':
                return
            grid[x][y] = '0'
            for dr, dc in dirs:
                dfs(dr + x, dc + y)
            return


        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        
        return count