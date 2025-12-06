import os

# global variables
initial_number = "50"
max_number = 100 # numbers from 0 to 99
current_number = int(initial_number)
password = 0

def rotate_dial(rotation: str) -> list[int]:
    """
    Rotates the dial given the rotation. <p>
    Returns true if the  number after the rotation is a 0, false otherwhise
    """
    direction = rotation[0]
    clicks = int(rotation[1:])

    global current_number
    n_pointed_zero = 0

    if direction == "L":
        # left rotation
        if current_number - clicks < 0:
            n_pointed_zero = abs(int((current_number - clicks) / max_number ))
            if current_number != 0: 
                n_pointed_zero += 1

        next_number = (current_number - clicks + max_number ) % max_number

    elif direction == "R":
        # right rotation
        n_pointed_zero = int(( current_number + clicks ) / max_number)
        next_number = (current_number + clicks) % max_number

    print("The Dial is rotated " + str(rotation) + " to point at " + str(next_number))

    # update current number
    current_number = next_number 

    # return next_number and number of zeros passed
    return [next_number, n_pointed_zero]


## input ##
def read_input(filename: str) -> list[str]: 
    try:
        with open(filename) as f:
            return list(map(clean_text,f.readlines()))
    except FileNotFoundError:
        return []

def clean_text (string: str) -> str:
    return string.replace("\n","")

def main():
    print(os.getcwd)
    global combinations,password
    combinations = read_input("input.txt")

    print("The Dial starts by pointing at " + initial_number)
    for r in combinations:
        next_number, nz = rotate_dial(r)
        if nz > 0:
            password += nz
        elif next_number == 0: 
            password += 1
          

    print("Password: ", password)


if __name__ == "__main__":
    main()

