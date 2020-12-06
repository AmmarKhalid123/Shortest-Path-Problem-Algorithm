from util import PriorityQueue
import time

def inClosed(node, closed):
    for i, j in closed.items():
        if i == node:
            return True
    return False

def getg(problem, currentState, c=0):
    if problem.start == currentState.name:
        return c
    else:
        node = problem.findNode(currentState.parent)
        c += problem.getDistance(node, currentState)
        return getg(problem, problem.findNode(currentState.parent), c)

def backtrack(problem, currentState, start, actions=[]):
    if start.name == currentState.name:
        actions.append(currentState.name)
        return actions
    else:
        actions.append(currentState.name)
        return backtrack(problem, problem.findNode(currentState.parent), start, actions)

def aStarSearch(problem):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = time.time()
    frontier = PriorityQueue()
    frontier.push(problem.getStartState(), 0)
    closed = {}
    
    while not(frontier.isEmpty()):
        currentState = frontier.pop()
        closed[currentState] = currentState.name
        if problem.isGoalState(currentState):
            break
        for node, action, stepCost in problem.getSuccessors(currentState):
            if not(inClosed(node, closed)):
                totalCost = stepCost + problem.getHeuristic(node) + getg(problem, currentState)
                if frontier.inPQ(node):
                    x = frontier.update(node, totalCost, currentState.name)
                    if x:
                        node.parent = currentState.name
                else:
                    node.parent = currentState.name
                    frontier.push(node, totalCost)
    end = time.time()
    "*** YOUR A* CODE HERE ***"
    actions = backtrack(problem, currentState, problem.getStartState())
    # print(actions[::-1])
    actions = actions[::-1]
    print(problem.getCostOfActions(actions))
    print("Runtime of A star: {}".format(end - start))


