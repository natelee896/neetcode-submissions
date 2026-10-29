class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        fresh = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0
        
        minutes = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            length = len(q)

            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        q.append((nr, nc))
                        grid[nr][nc] = -1 
                        fresh -= 1
            minutes += 1
        
        return minutes - 1 if fresh == 0 else -1

        