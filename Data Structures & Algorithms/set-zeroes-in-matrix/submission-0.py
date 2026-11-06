class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # we care about the original zeros
        m = len(matrix)
        n = len(matrix[0])

        columns = set()
        rows = set()

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    columns.add(c)
                    rows.add(r)
        
        for row in rows:
            for c in range(n):
                matrix[row][c] = 0
        
        for c in columns:
            for r in range(m):
                matrix[r][c] = 0
    
        return 
        