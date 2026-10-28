class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False

        m = len(board)
        n = len(board[0])

        visited = set()

        def dfs(r, c, i):  
            if i == len(word):
                return True
            
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i] or (r,c) in visited:
                return False

            visited.add((r, c))

            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            visited.remove((r, c))
            return found


        for x in range(m):
            for y in range(n):
                if board[x][y] in word:
                    result = dfs(x, y, 0)
                    if result:
                        return True
        
        return False
            