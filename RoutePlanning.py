from Node import Node
from search import SearchProblem

class RoutePlanning(SearchProblem):
    def __init__(self, start, end):
        self.nodes = []
        self.start = start
        self.end = end
        with open("./cities.csv", "r") as f:
            for i in f.readlines():
                self.nodes.append(Node(i.rstrip()))

        with open("./heuristics.csv", "r") as f:
            allCities = f.readline()[1:].split(',')
            allCities[-1] = allCities[-1].rstrip()
            for i in f.readlines():
                abc = i.split(',')
                city = abc[0]
                heuristic = {}
                for j in range(len(abc[1:])):
                    heuristic[allCities[j]] = int(abc[j+1])
                node = self.findNode(city)
                if node == False:
                    print("Error while setting heuristics of city" + city)
                    return
                node.heuristic = heuristic
        
        with open("./Connections.csv", "r") as f:
            allCities = f.readline()[1:].split(',')
            allCities[-1] = allCities[-1].rstrip()
            for i in f.readlines():
                abc = i.split(',')
                city = abc[0]
                child = {}
                for j in range(len(abc[1:])):
                    if int(abc[j+1]) != -1:
                        child[allCities[j]] = int(abc[j+1])
                node = self.findNode(city)
                if node == False:
                    print("Error while setting connections of city" + city)
                    return
                node.children = child

    def findNode(self, name):
        for i in self.nodes:
            if i.name == name:
                return i
        print("Node not found for city" + name)
        return False

    def getDistance(self, node, currentState):
        return node.children[currentState.name]

    
    def getHeuristic(self, state):
        # print(state.name,state.heuristic)
        if state.heuristic != {}:
            return state.heuristic[self.end]
        print("heuristic is empty for, "+state.name)
        return False

    def getStartState(self):
        for i in self.nodes:
            if i.name == self.start:
                return i
        print("Start state not found")
        return False
    
    def isGoalState(self, state):
        return state.name == self.end

    def getSuccessors(self, state):
        x = []
        for i, j in state.children.items():
            action = (state.name, i)
            a = self.findNode(i)
            if a != False:
                x.append((a, action, j))
            else:
                return False
        return x

    def getCostOfActions(self, actions):
        cost = 0
        for i in range(len(actions) - 1):
            node = self.findNode(actions[i])
            cost += node.children[actions[i + 1]]
        return cost

