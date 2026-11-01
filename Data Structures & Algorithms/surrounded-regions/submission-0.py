class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Work outside to in
        # Go through the borders first, then mark those as visited with dfs. 
        # Then mark everything else as 0

        m = len(board)
        n = len(board[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = set()
        def dfs(r, c):
            if (r, c) in visited or board[r][c] != 'O':
                return 
            visited.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    dfs(nr, nc)
            return
        
        # top row
        for c in range(n):
            dfs(0, c)
            dfs(m - 1, c)
        
        # left col
        for r in range(m):
            dfs(r, 0) 
            dfs(r, n - 1)
        
        # Then go through the entire grid
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and (r ,c) not in visited:
                    board[r][c] = 'X'
        
        return