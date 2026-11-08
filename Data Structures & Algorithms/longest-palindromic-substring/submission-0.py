class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP: from this index, how far can I expand outwards as a palindrome
        n = len(s)

        result = ""
        bestLength = -1
        
        def expand(left, right):
            while 0 <= left and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(n):
            result = max(result, expand(i, i), expand(i, i + 1), key = len)

        return result
            
        