class Node:
    def __init__(self, state, command, depth, last_moved_car, parent):
        self.state = state
        self.command = command
        self.depth = depth
        self.last_moved_car = last_moved_car
        self.parent = parent
        self.children = []
