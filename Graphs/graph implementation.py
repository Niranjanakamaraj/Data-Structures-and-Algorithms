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
            
if __name__ == "__main__":
    G = Graph()
    G.addEdge('A', 'B')
    G.addEdge('A', 'C')
    G.addEdge('B', 'C')
    G.addEdge('C', 'D')

    G.printGraph()

