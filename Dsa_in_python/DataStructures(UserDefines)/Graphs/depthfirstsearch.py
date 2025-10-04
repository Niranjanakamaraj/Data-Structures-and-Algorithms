class Graph:
    def __init__(self):
        self.graph = {}                              # Initializing graph as a dictionary

    def addVertex(self, vertex):
        if vertex not in self.graph:                 # Checking if vertex doesn't exist
            self.graph[vertex] = []                  # Assigning an empty list to represent edges

    def addEdge(self, src, dest):
        self.addVertex(src)                          # Adding the vertices if they don't already exist
        self.addVertex(dest)
        self.graph[src].append(dest)                 # Adding an edge from src to dest (undirected graph assumption)
        self.graph[dest].append(src)

    def printGraph(self):
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")

    def dfs_visited(self, vertex, visited):
        visited.add(vertex)                          # Marking the current vertex as visited
        print(vertex, end=" ")                      

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:              # Visiting unvisited neighbors
                self.dfs_visited(neighbor, visited)  # Recursively visiting each neighbor

    def dfs(self, start_vertex):
        visited = set()                              # keeping track of visited vertices
        self.dfs_visited(start_vertex, visited)      # Calling recursively

if __name__ == "__main__":
    G = Graph()
    G.addEdge('A', 'B')
    G.addEdge('A', 'C')
    G.addEdge('B', 'C')
    G.addEdge('C', 'D')

    G.printGraph()
    print("DFS traversal starting from vertex A:")
    G.dfs('A')
    print("\nDFS traversal starting from vertex B:")
    G.dfs('B')
    print("\nDFS traversal starting from vertex C:")
    G.dfs('C')
    print("\nDFS traversal starting from vertex D:")
    G.dfs('D')