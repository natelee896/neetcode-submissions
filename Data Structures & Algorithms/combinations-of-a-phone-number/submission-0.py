class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(start, path):
            if path and len(path) == len(digits):
                result.append("".join(path))
                return
            
            for i in range(start, len(digits)):
                for letter in phone[digits[i]]:
                    path.append(letter)
                    backtrack(i + 1, path)
                    path.pop()
            
            return
        
        backtrack(0, [])
        return result
