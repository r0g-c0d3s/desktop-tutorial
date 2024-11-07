7. Write a program that implements Prim's algorithm to generate minimum cost spanning Tree.

def find_min_edge(matrix, Vt): min_edge None min_weight = float("inf") V = len(matrix)

for u in Vt:

for v in range(V): if v not in Vt and matrix[u][v] > 0 and matrix[u][v] < min_weight: min_edge = (u, v, matrix[u][v]) min_weight matrix[u][v] return min_edge

def prim(matrix): V = len(matrix) start_vertex = 0 Vt = (start_vertex) Et= total_weight = 0

while len(Vt) <V:

min_edge = find_min_edge(matrix, Vt) if min_edge is None: break u, v, weight = min_edge Vt.add(v) Et.append((u, v, weight)) total_weight += weight return Et, total_weight

def print_minimum_spanning_tree(minimum_spanning_tree, total_weight): print("\nMinimum Spanning Tree:") for u, v, weight in minimum_spanning_tree: print(f"Edge: (u + 1}-{v+1), Weight: (weight)")

print(f"Total Weight of MST: (total_weight)")

num_vertices = int(input("Enter the number of vertices: ")) graph = [[ print("Enter the weight adjacency Matrix:")

for_in range(num_vertices): row = list(map(int, input(f"Enter weight of the vertex + 1}: ").split())) graph.append(row) minimum_spanning_tree, total_weight = prim(graph) print_minimum_spanning_tree(minimum_spanning_tree, total_weight)