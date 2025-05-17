def greedy_tsp(dist_matrix, start_index):
    n = len(dist_matrix)
    visited = [False] * n
    path = [start_index]
    visited[start_index] = True

    current = start_index
    while len(path) < n:
        next_city = min(
            [(i, dist_matrix[current][i]) for i in range(n) if not visited[i]],
            key=lambda x: x[1]
        )[0]
        path.append(next_city)
        visited[next_city] = True
        current = next_city

    path.append(start_index)  # Return to start
    return path

def total_path_length(path, dist_matrix):
    return sum(dist_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
