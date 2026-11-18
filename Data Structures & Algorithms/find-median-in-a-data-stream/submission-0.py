class MedianFinder:

    def __init__(self):
        # maxHeap takes left side, minHeap takes right
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # when we need to add a num, we should add to the maxHeap then rebalance to minHeap
        if self.maxHeap and num > self.maxHeap[0]:
            heapq.heappush(self.maxHeap, num)
        else:
            heapq.heappush(self.minHeap, -num)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
            

    def findMedian(self) -> float:
        if len(self.minHeap) > len(self.maxHeap):
            return -self.minHeap[0]
        elif len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        else:
            return (-1 * self.minHeap[0] + self.maxHeap[0]) / 2