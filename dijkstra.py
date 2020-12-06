from pqdict import minpq
import time
class Graph:
    def __init__(self):
        self.nodes = {}
        with open("./cities.csv", "r") as f:
            for i in f.readlines():
                self.nodes[i.rstrip()] = {}
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
                            self.nodes[city][allCities[j]] = int(abc[j+1])
g = Graph()

def dijkstra(graph, source, target=None):
    dist = {}  #lengths of the shortest paths to each node
    pred = {}  #predecessor node in each shortest path

    # Store distance scores in a priority queue dictionary
    pq = minpq()
    for node in graph:
        if node == source:
            pq[node] = 0
        else:
            pq[node] = float('inf')
            
    # popitems always pops out the node with min score
    # Removing a node from pqdict is O(log n).
    for node, min_dist in pq.popitems():
        dist[node] = min_dist
        if node == target:
            break
        for neighbor in graph[node]:
            if neighbor in pq:
                new_score = dist[node] + graph[node][neighbor]
                if new_score < pq[neighbor]:
                    # Updating the score of a node is O(log n) using pqdict.
                    pq[neighbor] = new_score
                    pred[neighbor] = node
    return dist, pred

def shortest_path(graph, source, target):
    dist, pred = dijkstra(graph, source, target)
    end = target
    path = [end]
    while end != source:
        end = pred[end]
        path.append(end)        
    path.reverse()
    return path


def dijkstra_final(source, dest):
    start = time.time()
    dist, pred = dijkstra(g.nodes, source)
    print(dist[dest])
    end = time.time()
    print("Runtime of Dijkstra: {}".format(end - start))

def print_path(s, d):
    print("Path: ", shortest_path(g.nodes, s, d))
