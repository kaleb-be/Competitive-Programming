class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        degrees = {}
        
        for edge in edges:
            u, v = edge
            degrees[u] = degrees.get(u, 0) + 1
            degrees[v] = degrees.get(v, 0) + 1
        
        center = max(degrees, key=degrees.get)
        
        return center
