import math

graph = {'A':{'B':10, 'C':3},
        'B':{'C':1, 'D':2},
        'C':{'B':4, 'D':8, 'E': 2},
        'D':{'E':7},
        'E':{'D':9}
}

def dijkstra(graph, start, goal):
  shortest_distance = {}
  predecessor = {}
  unseenNodes = graph
  infinity = math.inf
  path = []
  for node in unseenNodes:
    shortest_distance[node] = infinity
  shortest_distance[start] = 0
  #print(shortest_distance)
  
  while unseenNodes:
    minNode = None
    for node in unseenNodes:
      if minNode is None:
        minNode = node
      elif shortest_distance[node] < shortest_distance[minNode]:
        minNode = node
        
    for childNode, weight in graph[minNode].items():
      if weight + shortest_distance[minNode] < shortest_distance[childNode]:
        shortest_distance[childNode] = weight + shortest_distance[minNode]
        #predecessor[childNode] = minNode
        #print(shortest_distance)
        #print("................................")
        #print("unseenNodes are ", unseenNodes)
    unseenNodes.pop(minNode)
  print(shortest_distance)
  print("Shortest distance from ",start, " to ", goal," is ",shortest_distance[goal])
  
  
  
dijkstra(graph, 'E', "A")
