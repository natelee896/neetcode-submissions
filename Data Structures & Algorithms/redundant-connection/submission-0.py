class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [n for n in range(len(edges) + 1)]
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            xRoot, yRoot = find(x), find(y)
            if xRoot == yRoot:
                return False
            parent[xRoot] = yRoot
            return True
        
        for u, v in edges:
            if not union(u, v):
                return [u, v]
        
        return [0, 0]

        