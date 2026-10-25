from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        freq = defaultdict(int)

        result = 0
        left = 0
        for right in range(len(s)):
            freq[s[right]] += 1

            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
        
        return result
