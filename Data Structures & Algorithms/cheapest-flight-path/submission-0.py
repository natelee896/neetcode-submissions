class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for from_air, to_air, price in flights:
            graph[from_air].append((price, to_air))

        minHeap = [(0, 0, src)]
        result = 0
        best_flights = {}
        

        while minHeap:
            cost, used, airport = heapq.heappop(minHeap)
            if airport == dst:
                return cost
            if used == k + 1:
                continue 
            if airport in best_flights and best_flights[airport] <= used:
                continue
            
            
            best_flights[airport] = used

            for price, neighbor in graph[airport]:
                heapq.heappush(minHeap, (cost + price, used + 1, neighbor))
            
        return -1

        