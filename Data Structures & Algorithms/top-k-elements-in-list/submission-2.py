class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        minHeap = []

        for key in freq:
            heapq.heappush(minHeap, (freq[key], key))

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        result = []
        while minHeap:
            count, key = heapq.heappop(minHeap)
            result.append(key)
                
        return result