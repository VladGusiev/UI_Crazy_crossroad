import hashlib
import copy
from node import Node
from car import Car

# ------------- CARS LAYOUTS ------------------------------
# ----------- FROM TASK SITE ------------------------------
# red = Car("red", 2, 2, 3, "h")
# orange = Car("orange",2, 1,1, "h")
# yellow = Car("yellow", 3, 1, 2, "v")
# pink = Car("pink", 2, 1, 5, "v")
# green = Car("green", 3, 4, 2, "v")
# blue = Car("blue", 3, 3, 6, "h")
# grey = Car("grey", 2, 5, 5, "h")
# violet = Car("violet", 3, 6, 1, "v")

# --------- 10 STEP SOLUTION ------------------
# red = Car("red", 2, 2, 3, "h")
# violet = Car("violet", 3, 6, 1, "v")
# green = Car("green", 2, 4, 3, "h")
# blue = Car("blue", 3, 1, 3, "v")
# yellow = Car("yellow", 2, 5, 5, "v")
# lightblue = Car("lightblue", 2, 5, 1, "v")

# -------- NO SOLUTION -----------------
# red = Car("red", 2, 2, 3, "h")
# orange = Car("orange", 2, 3, 5, "v")
# yellow = Car("yellow", 2, 1, 6, "h")
# pink = Car("pink", 3, 4, 6, "h")
# green = Car("green", 3, 5, 3, "v")
# blue = Car("blue", 3, 1, 1, "v")
# darkgrey = Car("darkgrey", 3, 3, 2, "v")
# cyan = Car("cyan", 3, 2, 1, "h")

# --------- Solution in 5 ----------------
# red = Car("red", 2, 1, 6, "h")
# orange = Car("orange", 3, 1, 2, "v")
# yellow = Car("yellow", 2, 3, 1, "v")
# pink = Car("pink", 2, 6, 3, "v")
# green = Car("green", 3, 3, 3, "h")
# blue = Car("blue", 2, 1, 1, "h")
# darkgrey = Car("darkgrey", 2, 5, 5, "h")
# cyan = Car("cyan", 3, 3, 4, "v")
def generate_cars():
    red = Car("red", 2, 2, 3, "h")
    orange = Car("orange",2, 1,1, "h")
    yellow = Car("yellow", 3, 1, 2, "v")
    pink = Car("pink", 2, 1, 5, "v")
    green = Car("green", 3, 4, 2, "v")
    blue = Car("blue", 3, 3, 6, "h")
    grey = Car("grey", 2, 5, 5, "h")
    violet = Car("violet", 3, 6, 1, "v")


    # lightblue = Car("lightblue", 2, 5, 1, "v")
    return [
        red,
        orange,
        yellow,
        pink,
        green,
        blue,
        grey,
        violet,
        # lightblue
        # darkgrey,
        # cyan
    ]


already_generated_states = []


# hashing of every parameter of the car, and not a whole car!
def hash_state(state):
    state_hash = ""
    for car in state:
        state_hash += hashlib.sha1(car.color.encode()).hexdigest()
        state_hash += hashlib.sha1(str(car.size).encode()).hexdigest()
        state_hash += hashlib.sha1(str(car.x).encode()).hexdigest()
        state_hash += hashlib.sha1(str(car.y).encode()).hexdigest()
        state_hash += hashlib.sha1(car.orientation.encode()).hexdigest()

    return state_hash


#  -------------------- MOVING RIGHT! -----------------------------------
def right(state, car, move_by):
    starting_car_pos = copy.deepcopy(car.x)
    # new_state = []
    for i in range(move_by):
        if not is_right_available(state, car, 1):
            car.x = starting_car_pos
            print("Cannot Move Car RIGHT!")
            # return state
            return False

        car.x += 1
    # for state_car in state:
    #     if state_car.color == car.color:
    #         new_state.append(car)
    #     else:
    #         new_state.append(state_car)

    print(car.color, "car was moved RIGHT!")
    # return new_state
    return True


def is_right_available(state, car, move_by):
    if car.orientation == "v": return False  # print("canoot perform operaion: 'right' on car: ", car, "with orientation: ", car.orientation)
    if car.x + car.size + move_by > 7: return False

    blocks_to_check = []
    iteration = 1

    # creating a list of potential new coordinates to check
    while (car.size - iteration) >= 0:
        blocks_to_check.append(car.x + move_by + (car.size - iteration))
        iteration += 1
    # print(blocks_to_check)

    # check other car in list if they are already located on coordinates
    for other_car in state:
        # skip our car
        if car.color == other_car.color:
            continue

        # check for orientation due to different approaches
        if other_car.orientation == "h":
            other_car_blocks = []
            i = 1
            # the only way horizontal car can be in the way is, its located on the same y level and on the same blocks
            if other_car.y == car.y:
                while (other_car.size - i) >= 0:
                    other_car_blocks.append(other_car.x + (other_car.size - i))
                    i += 1
                print(other_car.color + "car has HORIZONTAL coordinates: ", other_car_blocks)

                for block in blocks_to_check:
                    if block in other_car_blocks:
                        return False  # print(other_car.color, "is in the way!")
        else:
            other_car_blocks = []
            i = 1
            # array of other car blocks
            while (other_car.size - i) >= 0:
                other_car_blocks.append(other_car.y + (other_car.size - i))
                i += 1
            # print(other_car_blocks)

            for block in other_car_blocks:
                # some block might be in the way
                if block == car.y:
                    if other_car.x in blocks_to_check:
                        return False  # print(other_car.color, "is in the way!")
    # car.x = car.x + move_by
    # return print(car.color, "car was moved!")
    return True


#  -------------------- MOVING LEFT! -----------------------------------
def left(state, car, move_by):
    starting_car_pos = copy.deepcopy(car.x)
    # new_state = []
    for i in range(move_by):
        if not is_left_available(state, car, 1):
            car.x = starting_car_pos
            # return state and print("Cannot Move Car LEFT!")
            print("Cannot Move Car LEFT!")
            return False
        car.x -= 1
    # for state_car in state:
    #     if state_car.color == car.color:
    #         new_state.append(car)
    #     else:
    #         new_state.append(state_car)

    # return new_state and print(car.color, "car was moved LEFT!")
    print(car.color, "car was moved LEFT!")
    return True


def is_left_available(state, car, move_by):
    if car.orientation == "v": return False  # print("canoot perform operaion: 'right' on car: ", car, "with orientation: ", car.orientation)
    if car.x - move_by < 1: return False

    blocks_to_check = []
    iteration = 1

    # creating a list of potential new coordinates to check
    while (car.size - iteration) >= 0:
        blocks_to_check.append(car.x + car.size - iteration - move_by)
        iteration += 1
    # print(car.color, "Car has coordinates: ", blocks_to_check)

    # check other car in list if they are already located on coordinates
    for other_car in state:
        # skip our car
        if car.color == other_car.color:
            continue

        # check for orientation due to different approaches
        if other_car.orientation == "h":
            other_car_blocks = []
            i = 1
            # the only way horizontal car can be in the way is, its located on the same y level and on the same blocks
            if other_car.y == car.y:
                while (other_car.size - i) >= 0:
                    other_car_blocks.append(other_car.x + (other_car.size - i))
                    i += 1
                print(other_car.color + "car has HORIZONTAL coordinates: ", other_car_blocks)
                for block in blocks_to_check:
                    if block in other_car_blocks:
                        return False  # print(other_car.color, "is in the way!")
        else:
            other_car_blocks = []
            i = 1
            # array of other car blocks
            while (other_car.size - i) >= 0:
                other_car_blocks.append(other_car.y + (other_car.size - i))
                i += 1
            # print(other_car.color + "car has VERTICAL coordinates: ", other_car_blocks)
            # print(other_car_blocks)

            for block in other_car_blocks:
                # some block might be in the way
                if block == car.y:
                    # print(other_car.color, "is in the way")
                    # print(other_car.x)
                    # print(blocks_to_check)
                    if other_car.x in blocks_to_check:
                        return False  # print(other_car.color, "is in the way!")
    # car.x = car.x + move_by
    # return print(car.color, "car was moved!")
    return True


#  -------------------- MOVING UP! -----------------------------------
def up(state, car, move_by):
    starting_car_pos = copy.deepcopy(car.y)
    # new_state = []
    for i in range(move_by):
        # print(car.color, ": [", car.x, car.y, "]")
        if not is_above_available(state, car, 1):
            car.y = starting_car_pos
            print("Cannot Move Car UP!")
            return False # state and print("Cannot Move Car UP!")
        car.y -= 1
    # for state_car in state:
    #     if state_car.color == car.color:
    #         new_state.append(car)
    #     else:
    #         new_state.append(state_car)

    print(car.color, "car was moved UP!")
    # return new_state
    return True


def is_above_available(state, car, move_by):
    if car.orientation == "h": return False  # print("canoot perform operaion: 'right' on car: ", car, "with orientation: ", car.orientation)
    if car.y - move_by < 1: return False

    blocks_to_check = []
    iteration = 1

    # creating a list of potential new coordinates to check
    while (car.size - iteration) >= 0:
        blocks_to_check.append(car.y + car.size - iteration - move_by)
        iteration += 1
    # print(car.color, "Car will have coordinates: ", blocks_to_check)

    # check other car in list if they are already located on coordinates
    for other_car in state:
        # print(other_car.color)
        # skip our car
        if car.color == other_car.color:
            continue

            # !!!  TODO swap h and v case !!!
        # check for orientation due to different approaches
        if other_car.orientation == "v":
            other_car_blocks = []
            i = 1
            # the only way vertical car can be in the way is, its located on the same x level and on the same blocks
            if other_car.x == car.x:
                while (other_car.size - i) >= 0:
                    other_car_blocks.append(other_car.y + (other_car.size - i))
                    i += 1
                # print(other_car.color + "car has VERTICAL coordinates: ", other_car_blocks)
                for block in blocks_to_check:
                    if block in other_car_blocks:
                        return False  # print(other_car.color, "is in the way!")
        else:
            other_car_blocks = []
            i = 1
            # array of other car blocks
            while (other_car.size - i) >= 0:
                other_car_blocks.append(other_car.x + (other_car.size - i))
                i += 1
            # print(other_car.color + "car has HORIZONTAL coordinates: ", other_car_blocks)
            # print(other_car_blocks)

            for block in other_car_blocks:
                # some block might be in the way
                if block == car.x:
                    # print(other_car.color, "is in the way")
                    # print(other_car.x)
                    # print(blocks_to_check)
                    if other_car.y in blocks_to_check:
                        return False  # print(other_car.color, "is in the way!")
    # car.x = car.x + move_by
    # return print(car.color, "car was moved!")
    return True


#  -------------------- MOVING DOWN! -----------------------------------
def down(state, car, move_by):
    starting_car_pos = copy.deepcopy(car.y)
    # new_state = []
    for i in range(move_by):
        if not is_below_available(state, car, 1):
            car.y = starting_car_pos
            print("Cannot Move Car DOWN!")
            return False # state and print("Cannot Move Car DOWN!")
        car.y += 1
    # for state_car in state:
    #     if state_car.color == car.color:
    #         new_state.append(car)
    #     else:
    #         new_state.append(state_car)
    print(car.color, "car was moved DOWN!")
    # print(car.color, "y coord: ", car.y)
    # return new_state
    return True


def is_below_available(state, car, move_by):
    if car.orientation == "h": return False  # and print("canoot perform operaion: 'right' on car: ", car, "with orientation: ", car.orientation)
    # print(car.y + move_by + car.size-1)
    if car.y + move_by + car.size > 7: return False  # and print("out of range")

    blocks_to_check = []
    iteration = 1

    # creating a list of potential new coordinates to check
    while (car.size - iteration) >= 0:
        blocks_to_check.append(car.y + move_by + (car.size - iteration))
        iteration += 1
    # print(car.color, "Car will have coordinates: ", blocks_to_check)

    # check other car in list if they are already located on coordinates
    for other_car in state:
        # skip our car
        if car.color == other_car.color:
            continue

            # !!!  TODO swap h and v case !!!
        # check for orientation due to different approaches
        if other_car.orientation == "v":
            other_car_blocks = []
            i = 1
            # the only way vertical car can be in the way is, its located on the same x level and on the same blocks
            if other_car.x == car.x:
                while (other_car.size - i) >= 0:
                    other_car_blocks.append(other_car.y + (other_car.size - i))
                    i += 1
                # print(other_car.color + "car has VERTICAL coordinates: ", other_car_blocks)
                for block in blocks_to_check:
                    if block in other_car_blocks:
                        return False  # print(other_car.color, "is in the way!")
        else:
            other_car_blocks = []
            i = 1
            # array of other car blocks
            while (other_car.size - i) >= 0:
                other_car_blocks.append(other_car.x + (other_car.size - i))
                i += 1
            # print(other_car.color + "car has HORIZONTAL coordinates: ", other_car_blocks)
            # print(other_car_blocks)

            for block in other_car_blocks:
                # some block might be in the way
                if block == car.x:
                    # print(other_car.color, "is in the way")
                    # print(other_car.x)
                    # print(blocks_to_check)
                    if other_car.y in blocks_to_check:
                        return False  # print(other_car.color, "is in the way!")
    return True


def generate_states(root_node):
    root_state = copy.deepcopy(root_node.state)
    children_list = []

    for car in root_state:
        car_copy = copy.deepcopy(car)
        if car.orientation == "h":
            move_by = 1
            # check if move is possible
            while right(root_state, car, move_by):
                state_copy = copy.deepcopy(root_state)
                hashed_state = hash_state(state_copy)
                if hashed_state not in already_generated_states:
                    already_generated_states.append(hashed_state)
                    # root_node.children.append(Node(root_state))
                    children_list.append(Node(state_copy, root_node))
                    for state_car in state_copy:
                        print(state_car.color, "has coordinates: ", state_car.x, state_car.y)
                move_by += 1
                car.x, car.y = car_copy.x, car_copy.y

            move_by = 1
            car.x, car.y = car_copy.x, car_copy.y

            while left(root_state, car, move_by):
                state_copy = copy.deepcopy(root_state)
                hashed_state = hash_state(state_copy)
                if hashed_state not in already_generated_states:
                    already_generated_states.append(hashed_state)

                    # root_node.children.append(Node(root_state))
                    children_list.append(Node(state_copy, root_node))

                    for state_car in state_copy:
                        print(state_car.color, "has coordinates: ", state_car.x, state_car.y)
                move_by += 1
                car.x, car.y = car_copy.x, car_copy.y

        elif car.orientation == "v":
            move_by = 1
            # check if move is possible
            while up(root_state, car, move_by):
                state_copy = copy.deepcopy(root_state)
                hashed_state = hash_state(state_copy)
                if hashed_state not in already_generated_states:
                    already_generated_states.append(hashed_state)
                    # root_node.children.append(Node(root_state))
                    children_list.append(Node(state_copy, root_node))

                    for state_car in state_copy:
                        print(state_car.color, "has coordinates: ", state_car.x, state_car.y)
                move_by += 1
                car.x, car.y = car_copy.x, car_copy.y

            move_by = 1
            car.x, car.y = car_copy.x, car_copy.y

            while down(root_state, car, move_by):
                state_copy = copy.deepcopy(root_state)
                hashed_state = hash_state(state_copy)
                if hashed_state not in already_generated_states:
                    already_generated_states.append(hashed_state)
                    # root_node.children.append(Node(root_state))
                    children_list.append(Node(state_copy, root_node))

                    for state_car in state_copy:
                        print(state_car.color, "has coordinates: ", state_car.x, state_car.y)
                move_by += 1
                car.x, car.y = car_copy.x, car_copy.y

    # print("List of root nodes children: ", children_list)
    return children_list


# target is pos of red car with size 2: [x] -> [5]
# red car is always at position 0 in the list

# TODO This is just IDS, need to implement creation of the tree,
#  reduction of the duplicates and assigning of the children to parent
def find_solution(root_node, max_depth):
    if max_depth >= 1000:
        print("No solution was found!")
        exit(1)
    if root_node.state[0].x == 5:
        layer = 1
        print("Found Answer!")
        # for state_car in root_node.state:
        #     print(state_car.color, "has coordinates: ", state_car.x, state_car.y)
        while not root_node.parent == None:
            print(layer,  ": ---------------------------")
            for state_car in root_node.state:
                print(state_car.color, "has coordinates: ", state_car.x, state_car.y)
            # print("---------------------------")

            layer += 1
            root_node = root_node.parent

        return True  # check if red car is already at needed position

    if max_depth <= 0:
        print("reached max depth")
        return False  # reached max depth

    # print("Children list before generation: ", root_node.children)
    root_node.children = generate_states(root_node)
    # print("Children list after generation: ", root_node.children)

    # check of all children of the node
    for node in root_node.children:
        if find_solution(node, max_depth - 1):
            return True
    return False


def main():
    starting_state = generate_cars()
    current_state = copy.deepcopy(starting_state)

    root_node = Node(copy.deepcopy(current_state), None)
    already_generated_states.append(hash_state(starting_state))

    depth = 5
    while not find_solution(root_node, depth):
        depth += 1
        already_generated_states.clear()
        root_node.children.clear()
    print(depth)

    print(len(already_generated_states))


if __name__ == '__main__':
    main()
