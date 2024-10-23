def find_parent(parent, i):
    if parent[i] == i:
        return i
    else:
        return find_parent(parent, parent[i])

def kruskal(graph):
    num_vertices = len(graph)
    parent = list(range(num_vertices))
    edges = []

    # Collect all edges from the graph
    for u in range(num_vertices):
        for v in range(num_vertices):
            if graph[u][v] > 0:  # Only consider positive weights
                edges.append((u, v, graph[u][v]))

    # Sort edges based on their weights
    edges.sort(key=lambda x: x[2])
    
    mst = []
    
    for u, v, w in edges:
        parent_u = find_parent(parent, u)
        parent_v = find_parent(parent, v)

        if parent_u != parent_v:  # Check for cycle
            mst.append((u, v, w))
            parent[parent_u] = parent_v  # Union operation

    return mst

def print_mst(mst):
    total_weight = sum(w for _, _, w in mst)
    print("Minimum spanning tree using Kruskal's algorithm:")
    print("Edges Weight")

    for u, v, w in mst:
        print(f"{u}-{v} {w}")
    print(f"Total weight: {total_weight}")

def main():
    V = int(input("Enter the number of vertices: "))
    print("Enter the weighted adjacency matrix (enter 0 for no edges):")
    graph = [list(map(int, input().split())) for _ in range(V)]
    
    mst = kruskal(graph)
    print_mst(mst)

if __name__ == "__main__":
    main()
