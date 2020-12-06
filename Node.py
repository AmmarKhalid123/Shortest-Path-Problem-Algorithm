class Node:
    def __init__(self, name):
        self.name = name
        self.parent = ""
        self.children = {}
        self.heuristic = {}