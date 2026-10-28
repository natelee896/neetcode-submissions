class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def backtrack(openned, closed, path):
            if len(path) == 2 * n:
                result.append("".join(path))
                return
            
            if openned < n:
                path.append('(')
                backtrack(openned + 1, closed, path)
                path.pop()
            if closed < openned:
                path.append(')')
                backtrack(openned, closed + 1, path)
                path.pop()
        
        backtrack(0, 0, [])
        return result