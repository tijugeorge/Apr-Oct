#DFS traversal from a given graph 

from collections import defaultdict

class Graph:
  def __init__(self):
    self.graph = defaultdict(list)  # default dictionary to stor graph

  def addEdge(self, u, v):
    """funct to add adge to graph"""
    self.graph[u].append(v)

  def DFSUtil(self, v, visited):
    visited[v] = True #mark the current node as visited and print it
    print(v)

    for i in self.graph[v]:
      if visited[i] == False:
        self.DFSUtil(i, visited)

  def DFS(self, v):
    visited = [False]*(len(self.graph))   #mark all vertices as not visited
    self.DFSUtil(v, visited)  # call the recursive util funvtion to print DFS traversal

# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
print(g.graph)

