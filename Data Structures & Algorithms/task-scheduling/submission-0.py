class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # want to use up the most frequent task first

        freq = Counter(tasks)
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time