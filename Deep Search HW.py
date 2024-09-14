# DFS algorithm with simple UI interaction

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    # Mark the current node as visited
    visited.add(start)
    print(str(start) + " ", end="")

    # Recur for all the vertices adjacent to this vertex
    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)

def get_graph_input():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    print("Enter the edges for each node as space-separated integers.")
    print("For example, to add edges from node 0 to 1 and 2, enter: 0 1 2")

    for i in range(n):
        edges = input(f"Enter edges for node {i}: ").strip().split()
        graph[i] = list(map(int, edges[1:]))

    return graph

def main():
    print("=== Depth First Search (DFS) Algorithm ===\n")

    # Get graph from user
    graph = get_graph_input()

    # Display the graph for confirmation
    print("\nGraph Structure: ")
    for node, edges in graph.items():
        print(f"{node} -> {edges}")

    # Get starting node for DFS
    start_node = int(input("\nEnter the starting node for DFS traversal: "))

    # Perform DFS
    print("\nDFS Traversal Order:")
    dfs(graph, start_node)

if __name__ == '__main__':
    main()
