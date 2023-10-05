import hashlib
import copy
from node import Node
from car import Car


red = Car("red", 2, 2, 3, "h")
violet = Car("violet", 3, 6, 1, "v")
green = Car("green", 2, 4, 4, "h")
blue = Car("blue", 3, 1, 3, "v")
yellow = Car("yellow", 2, 5, 5, "v")
lightblue = Car("lightblue", 2, 5, 1, "v")

starting_state = [
    # red,
    # violet,
    # green,
    # blue,
    yellow,
    lightblue
]


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
    new_state = []
    for i in range(move_by):
        if not is_right_available(state, car, 1):
            car.x = starting_car_pos
            return state and print("Cannot Move Car RIGHT!")
        car.x += 1
    for state_car in state:
        if state_car.color == car.color:
            new_state.append(car)
        else:
            new_state.append(state_car)

    return new_state and print(car.color, "car was moved RIGHT!")


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
    new_state = []
    for i in range(move_by):
        if not is_left_available(state, car, 1):
            car.x = starting_car_pos
            return state and print("Cannot Move Car LEFT!")
        car.x -= 1
    for state_car in state:
        if state_car.color == car.color:
            new_state.append(car)
        else:
            new_state.append(state_car)

    return new_state and print(car.color, "car was moved LEFT!")


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
    new_state = []
    for i in range(move_by):
        # print(car.color, ": [", car.x, car.y, "]")
        if not is_above_available(state, car, 1):
            car.y = starting_car_pos
            return state and print("Cannot Move Car UP!")
        car.y -= 1
    for state_car in state:
        if state_car.color == car.color:
            new_state.append(car)
        else:
            new_state.append(state_car)

    print(car.color, "car was moved UP!")
    return new_state


def is_above_available(state, car, move_by):
    if car.orientation == "h": return False  # print("canoot perform operaion: 'right' on car: ", car, "with orientation: ", car.orientation)
    if car.y - move_by < 1: return False

    blocks_to_check = []
    iteration = 1

    # creating a list of potential new coordinates to check
    while (car.size - iteration) >= 0:
        blocks_to_check.append(car.y + car.size - iteration - move_by)
        iteration += 1
    print(car.color, "Car will have coordinates: ", blocks_to_check)

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
                print(other_car.color + "car has VERTICAL coordinates: ", other_car_blocks)
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
            print(other_car.color + "car has HORIZONTAL coordinates: ", other_car_blocks)
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
    new_state = []
    for i in range(move_by):
        if not is_below_available(state, car, 1):
            car.y = starting_car_pos
            return state and print("Cannot Move Car DOWN!")
        car.y += 1
    for state_car in state:
        if state_car.color == car.color:
            new_state.append(car)
        else:
            new_state.append(state_car)
    print(car.color, "car was moved DOWN!")
    print(car.color, "y coord: ", car.y)
    return new_state


def is_below_available(state, car, move_by):
    if car.orientation == "h": return False #  and print("canoot perform operaion: 'right' on car: ", car, "with orientation: ", car.orientation)
    # print(car.y + move_by + car.size-1)
    if car.y + move_by + car.size > 7: return False #  and print("out of range")

    blocks_to_check = []
    iteration = 1

    # creating a list of potential new coordinates to check
    while (car.size - iteration) >= 0:
        blocks_to_check.append(car.y + move_by + (car.size - iteration))
        iteration += 1
    print(car.color, "Car will have coordinates: ", blocks_to_check)

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
                print(other_car.color + "car has VERTICAL coordinates: ", other_car_blocks)
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
            print(other_car.color + "car has HORIZONTAL coordinates: ", other_car_blocks)
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

 # TODO Fix up and down!
def main():
    current_state = copy.deepcopy(starting_state)

    # right(current_state, red, 1)
    # right(current_state, red, 1)
    # left(current_state, red, 1)
    # left(current_state, red, 1)
    # left(current_state, red, 1)
    # up(current_state, yellow, 1)
    # up(current_state, yellow, 1)
    # up(current_state, yellow, 1)
    # up(current_state, yellow, 1)
    # up(current_state, yellow, 1)
    # up(current_state, yellow, 1)
    #
    down(current_state, lightblue, 12)
    down(current_state, lightblue, 3)
    down(current_state, lightblue, 1)
    down(current_state, lightblue, 1)

    # up(current_state, lightblue, 1)
    # up(current_state, lightblue, 1)
    # up(current_state, lightblue, 1)
    # up(current_state, lightblue, 1)
    # up(current_state, lightblue, 1)
    # up(current_state, lightblue, 1)
    # down(current_state, yellow, 1)
    # down(current_state, yellow, 1)


    # down(current_state, yellow, 1)
    # right(current_state, red, 4)
    # left(current_state, red, 4)


    # print(hash_state(current_state) == hash_state(right(current_state, red, 2)))
    # print(current_state[0].y)
    # print(move_right(current_state, red, 2)[0].y)



if __name__ == '__main__':
    main()
