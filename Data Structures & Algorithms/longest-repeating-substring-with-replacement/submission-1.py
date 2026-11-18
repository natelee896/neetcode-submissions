class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        result = 0

        left = 0
        maxf = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1
            maxf = max(maxf, freq[s[right]])

            while right - left + 1 - maxf > k:
                freq[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)

        return result