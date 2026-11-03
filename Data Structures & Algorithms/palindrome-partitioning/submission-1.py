class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(word):
            left = 0
            right = len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, path):
            if start == len(s):                       
                result.append(path.copy())                
                return

            for i in range(start, len(s)):
                piece = s[start:i + 1]                
                if not isPalindrome(piece):           
                    continue
                path.append(piece)                    
                backtrack(i + 1, path)                
                path.pop()
        
        backtrack(0, [])
        return result