class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        # four walls
        top = 0
        bottom = m - 1
        left = 0
        right = n - 1

        result = []

        while top <= bottom and left <= right:
            # top left to right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # right top to bottom
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1

            # bottom right to left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            
            # left bottom to top
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1
        
        return result