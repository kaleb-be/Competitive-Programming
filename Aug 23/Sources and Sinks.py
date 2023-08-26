def find_sources_and_sinks(adj_matrix):
    n = len(adj_matrix)
    sources = []
    sinks = []
    
    for vertex in range(n):
        if all(adj_matrix[i][vertex] == 0 for i in range(n)) and any(adj_matrix[vertex][j] == 1 for j in range(n)):
            sources.append(vertex + 1)
        
        if all(adj_matrix[vertex][j] == 0 for j in range(n)) and any(adj_matrix[i][vertex] == 1 for i in range(n)):
            sinks.append(vertex + 1)
    
    return sources, sinks

n = int(input())
adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

sources, sinks = find_sources_and_sinks(adj_matrix)

print(len(sources), *sources)
print(len(sinks), *sinks)
