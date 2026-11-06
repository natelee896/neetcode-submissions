class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for from_air, to_air in tickets:
            graph[from_air].append(to_air)
        
        for key in graph:
            graph[key].sort(reverse = True)

        result = []

        def dfs(city):
            while graph[city]:
                destination = graph[city].pop()
                dfs(destination)
            result.append(city)
        
        dfs('JFK')
        return result[::-1]