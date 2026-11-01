class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window
        result = 0

        freqSet = set(s)

        for c in freqSet:
            count = 0
            left = 0

            for right in range(len(s)):
                if s[right] == c:
                    count += 1
                
                while right - left + 1 - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1
                
                result = max(right - left + 1, result)
            
        return result