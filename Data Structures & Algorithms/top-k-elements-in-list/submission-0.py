from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        mostFreq = sorted(freq, key = lambda x: freq[x], reverse = True)

        return mostFreq[:k]


