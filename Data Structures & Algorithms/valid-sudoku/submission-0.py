class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row, col, then every 3 by 3 square

        # Rows check

        for r in range(9):
            currNum = set()
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in currNum:
                        return False
                    else:
                        currNum.add(board[r][c])
        
        # Col check
        for c in range(9):
            currNum = set()
            for r in range(9):
                if board[r][c] != ".":
                    if board[r][c] in currNum:
                        return False
                    else:
                        currNum.add(board[r][c])
        
        # 3 by 3 now
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                currNum = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != '.':
                            if board[i][j] in currNum:
                                return False
                            else:
                                currNum.add(board[i][j])
        
        return True