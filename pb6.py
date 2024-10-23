import sys

def nearest_neighbor(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    current_vertex = 0
    visited[current_vertex] = True
    tour = [current_vertex + 1]
    total_distance = 0

    for _ in range(num_vertices - 1):
        nearest_vertex = None
        min_distance = sys.maxsize

        for vertex in range(num_vertices):
            if not visited[vertex] and graph[current_vertex][vertex] < min_distance:
                nearest_vertex = vertex
                min_distance = graph[current_vertex][vertex]

        tour.append(nearest_vertex + 1)
        total_distance += min_distance
        visited[nearest_vertex] = True
        current_vertex = nearest_vertex

    # Return to the starting point
    tour.append(tour[0])
    total_distance += graph[current_vertex][tour[0] - 1]
    return tour, total_distance

def main():
    n = int(input("Enter the number of nodes: "))
    graph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            graph[i][j] = int(input(f"Enter the distance from node {i + 1} to node {j + 1}: "))

    tour, total_distance = nearest_neighbor(graph)
    print(f"Optimal Tour: {tour}")
    print(f"Total Distance: {total_distance}")

if __name__ == "__main__":
    main()
