class Graph:
    def __init__(self, n):
        self.adj_list = [[] for _ in range(n + 1)]
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def vertex(self, u):
        adjacent_vertices = self.adj_list[u]
        if adjacent_vertices:
            print(" ".join(map(str, adjacent_vertices)))
        else:
            print()

n = int(input())
k = int(input())

graph = Graph(n)

for _ in range(k):
    operation = input().split()
    if operation[0] == '1':
        u, v = map(int, operation[1:])
        graph.add_edge(u, v)
    elif operation[0] == '2':
        u = int(operation[1])
        graph.vertex(u)
