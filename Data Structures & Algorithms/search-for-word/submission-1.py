class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = False

        m = len(board)
        n = len(board[0])

        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[i] or (r, c) in visited:
                return False
            
            visited.add((r, c))
            found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1))
            visited.remove((r, c))
            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] in word:
                    result = dfs(r, c, 0)
                    if result:
                        return True
        
        return False