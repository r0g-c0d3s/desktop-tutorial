3. Write a program to find shortest paths to other vertices using Dijkstra's algorithm.

def dijkstra(graph, start):

num_vertices = len(graph)

distances [float('inf)] num_vertices

penultimate_vertices = [None] num_vertices

distances[start] = 0

visited [False] num_vertices

for_in range(num_vertices): min_distance = float('inf)

min_vertex = -1

for v in range(num_vertices): if not visited[v] and distances[v] <min_distance: min_distance distances[v] min_vertexv

if min vertex = -1:

break

visited[min_vertex] = True

for v in range(num_vertices): if not visited[v] and graph[min_vertex][v] > 0: new_distance = distances[min_vertex] + graph[min_vertex][v] if new_distance < distances[v]: distances[v] = new_distance penultimate_vertices[v] = min_vertex

return distances, penultimate vertices

def get_path(penultimate_vertices, destination): path = [destination] while penultimate_vertices[destination] is not None: destination penultimate_vertices[destination] path.insert(0, destination)

return path

no_vertices = int(input("Enter the number of vertices: ")) graph = []

print("Enter the weight adjacency matrix:") for i in range(no_vertices):

row= list(map(int, input(f"Enter the weights of the vertices for vertex (i): ").split())) graph.append(row)

start_vertex = int(input("Enter the start vertex (0 to (no_vertices-1}): ")) distances, penultimate_vertices dijkstra(graph, start_vertex)

for vertex, distance in enumerate(distances): if vertex != start_vertex path_to_vertex = get_path(penultimate_vertices, vertex) print(f"Shortest distance from (start_vertex} to {vertex) is (distance), path: (path_to_vertex}")