class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check every row, then every col 

        n = 9

        # Rows first
        for r in range(n):
            visited = set()
            for c in range(n):
                if board[r][c] == '.':
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])
        
        # Cols next
        for c in range(n):
            visited = set()
            for r in range(n):
                if board[r][c] == '.':
                    continue
                if board[r][c] in visited:
                    return False
                visited.add(board[r][c])
        
        # 3 by 3s next
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                visited = set()
                for x in range(r, r + 3):
                    for y in range(c, c + 3):
                        if board[x][y] == '.':
                            continue
                        if board[x][y] in visited:
                            return False
                        visited.add(board[x][y])
        
        return True