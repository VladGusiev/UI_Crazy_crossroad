import hashlib
import copy
from node import Node
from car import Car


red = Car("red", 2, 2, 3, "h")
violet = Car("violet", 3, 6, 1, "v")
green = Car("green", 2, 4, 4, "v")

starting_state = [
    red,
    violet,
    green
]


def hash_state(state):
    state_hash = ""
    for car in state:
        state_hash += hashlib.sha1(car.color.encode()).hexdigest()
        state_hash += hashlib.sha1(str(car.size).encode()).hexdigest()
        state_hash += hashlib.sha1(str(car.x).encode()).hexdigest()
        state_hash += hashlib.sha1(str(car.y).encode()).hexdigest()
    return state_hash


# hashing of every parameter of the car, and not a whole car!

# MOVING RIGHT!
def move_right(state, car, move_by):
    starting_car_pos = copy.deepcopy(car.x)
    new_state = []
    for i in range(move_by):
        if not right(state, car, 1):
            car.x = starting_car_pos
            return state  # and print("Cannot Move Car!")
        car.x += 1
    for state_car in state:
        if state_car.color == car.color:
            new_state.append(car)
        else:
            new_state.append(state_car)

    return True # and print(car.color, "car was moved!")


# TODO MOVEMENT STEP BY STEP !!!
def right(state, car, move_by):
    if car.orientation == "v": return False  # print("canoot perform operaion: 'right' on car: ", car, "with orientation: ", car.orientation)
    if car.x + car.size + move_by > 6: return False

    blocks_to_check = []
    iteration = 1

    # creating a list of potential new coordinates to check
    while (car.size - iteration) >= 0:
        blocks_to_check.append(car.x + move_by + (car.size - iteration))
        iteration += 1
    print(blocks_to_check)

    # check other car in list if they are already located on coordinates
    for other_car in state:
        # skip our car
        if car.color == other_car.color:
            continue

        # check for orientation due to different approaches
        if other_car.orientation == "h":
            other_car_blocks = []
            i = 0
            # the only way horizontal car can be in the way is, its located on the same y level and on the same blocks
            if other_car.y == car.y:
                while (other_car.size - i) >= 0:
                    other_car_blocks.append(other_car.x + (other_car.size - i))
                    i += 1
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


def up(state, car, move_by):
    if car.orientation == "h": return print("canoot perform operaion: 'up' on car: ", car.color, "with orientation: ",
                                            car.orientation)

    blocks_to_check = []
    iteration = 1

    while (car.size - iteration) == 0:
        blocks_to_check.append(car.y + move_by + (car.size - iteration))
        iteration += 1
    print(blocks_to_check)
    for other_car in state:
        if car.color == other_car.color:
            continue
        if other_car.y in blocks_to_check:
            return print(other_car.color, "is in the way!")
    car.y = car.y + move_by
    return print(car.color, "car was moved!")


def main():
    current_state = copy.deepcopy(starting_state)
    # print(red.orientation == "h")
    # print(red.x)
    # right(current_state, red, 1)
    # right(current_state, red, 1)
    # right(current_state, red, 1)
    print(hash_state(current_state))
    move_right(current_state, red, 3)
    move_right(current_state, red, 1)
    move_right(current_state, red, 1)
    print(hash_state(current_state) == hash_state(move_right(current_state, red, 2)))
    # print(current_state[0].y)
    # print(move_right(current_state, red, 2)[0].y)



if __name__ == '__main__':
    main()
