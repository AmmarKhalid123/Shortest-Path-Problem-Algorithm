from A_star import aStarSearch
from RoutePlanning import RoutePlanning
from BellmanFord import Bellman_final
from dijkstra import dijkstra_final, print_path



def final(src, dest):
    print("Shortest distance from {} to {}".format(src, dest))
    a = RoutePlanning(src, dest)
    print("From A star:")
    aStarSearch(a)
    print("From Bellman Ford:")
    Bellman_final(src, dest)
    print("From Dijkstra:")
    dijkstra_final(src, dest)
    print_path(src, dest)

final("Islamabad", "Hunza")