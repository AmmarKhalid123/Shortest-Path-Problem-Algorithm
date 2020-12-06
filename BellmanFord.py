from pqdict import minpq
import time

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        with open("./cities.csv", "r") as f:
            for i in f.readlines():
                self.nodes.append(i.rstrip())
        with open("./Connections.csv", "r") as f:
            allCities = f.readline()[1:].split(',')
            allCities[-1] = allCities[-1].rstrip()
            for i in f.readlines():
                abc = i.split(',')
                city = abc[0]
                child = {}
                for j in range(len(abc[1:])):
                    if int(abc[j+1]) != -1:
                        if int(abc[j+1]) != 0:
                            self.edges.append((city, allCities[j], int(abc[j+1])))
g = Graph()

def BellmanFord(graph, src, dest):
        start = time.time()
        # Step 1: Initialize distances from src to all other vertices  
        # as INFINITE  
        dist = {}
        for node in graph.nodes:
                if node == src:
                        dist[node] = {0}
                else:
                        dist[node] = float('inf')
        dist[src] = 0
  
  
        # Step 2: Relax all edges |V| - 1 times. A simple shortest  
        # path from src to any other vertex can have at-most |V| - 1  
        # edges  
        for _ in range(len(graph.nodes) - 1): 
            # Update dist value and parent index of the adjacent vertices of  
            # the picked vertex. Consider only those vertices which are still in  
            # queue
            for u, v, w in graph.edges:  #u=source v=nighbour w=weights
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:  
                        dist[v] = dist[u] + w
  
        # Step 3: check for negative-weight cycles. The above step  
        # guarantees shortest distances if graph doesn't contain  
        # negative weight cycle. If we get a shorter path, then there  
        # is a cycle.  
  
        for u, v, w in graph.edges:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print("Graph contains negative weight cycle") 
                        return
        end = time.time()
        print(dist[dest])
        print("Runtime of Bellman: {}".format(end - start))
        # print all distance
def Bellman_final(src, dest):
        BellmanFord(g, src, dest)