class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, t in times:
            graph[u].append((t, v))
        
        minHeap = [(0, k)]
        visited = set()
        effort = 0

        while minHeap:
            w1, node1 = heapq.heappop(minHeap)
            if node1 in visited:
                continue
            visited.add(node1)
            effort = w1

            for w2, node2 in graph[node1]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, node2))
        
        return effort if len(visited) == n else -1