def adjacency_matrix_to_list(adj_matrix):
    n = len(adj_matrix)
    adj_list = []
    
    for i in range(n):
        neighbors = []
        for j in range(n):
            if adj_matrix[i][j] == 1:
                neighbors.append(j + 1)
        adj_list.append(neighbors)
    
    return adj_list

n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

adj_list = adjacency_matrix_to_list(adj_matrix)

for neighbors in adj_list:
    print(len(neighbors), *neighbors)
