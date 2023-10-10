class Node:
    def __init__(self, state, parent, operation):
        self.state = state
        self.parent = parent
        self.operation = operation
        self.children = []
