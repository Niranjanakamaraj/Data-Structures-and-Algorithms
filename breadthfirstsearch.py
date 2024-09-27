class Graph:
    def __init__(self):
        self.graph = {}                              # Initializing graph as a dictionary

    def addVertex(self, vertex):
        if vertex not in self.graph:                 # Check if vertex doesn't exist
            self.graph[vertex] = []                  # Assign an empty list to represent edges

    def addEdge(self, src, dest):
                                                     # Add the vertices if they don't already exist
        self.addVertex(src)
        self.addVertex(dest)
        
                                                     # Add an edge from src to dest (undirected graph assumption)
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def printGraph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def bfs(self, start_vertex):
        visited = set()                               # Set to keep track of visited vertices
        queue = []                                    # Queue for BFS

        queue.append(start_vertex)                    # Start with the given vertex
        visited.add(start_vertex)                     # Mark the start vertex as visited

        while queue:
            vertex = queue.pop(0)                     # Dequeue a vertex
            print(vertex, end=" ")                    # Process the vertex

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:           # Visiting unvisited neighbors
                    queue.append(neighbor)            # Enqueue the neighbor
                    visited.add(neighbor)             # Mark neighbor as visited

if __name__ == "__main__":
    G = Graph()
    G.addEdge('A', 'B')
    G.addEdge('A', 'C')
    G.addEdge('B', 'C')
    G.addEdge('C', 'D')

    G.printGraph()

    print("\nBFS traversal starting from vertex A:")
    G.bfs('B')
    print("\nBFS traversal starting from vertex B:")
    G.bfs('A')
    print("\nBFS traversal starting from vertex C:")
    G.bfs('C')
    print("\nBFS traversal starting from vertex D:")
    G.bfs('D')