# global variables
initial_number = "50"
max_number = 100 # numbers from 0 to 99
current_number = int(initial_number)
password = 0

def rotate_dial(rotation: str):
    """
    Rotates the dial given the rotation. <p>
    Returns true if the  number after the rotation is a 0, false otherwhise
    """
    direction = rotation[0]
    clicks = int(rotation[1:])

    global current_number

    if direction == "L":
        # left rotation
        next_number = (current_number - clicks + max_number ) % max_number

    elif direction == "R":
        # right rotation
        next_number = (current_number + clicks) % max_number

    current_number = next_number # update current number

    print("The Dial is rotated " + str(rotation) + " to point at " + str(next_number))
    return next_number == 0


## input ##
def read_input(filename: str) -> list[str]: 
    try:
        with open(filename) as f:
            return list(map(clean_text,f.readlines()))
    except FileNotFoundError as ex:
        print(ex)  
        return []

def clean_text (string: str) -> str:
    return string.replace("\n","")

def main():
    global combinations
    combinations = read_input("input.txt")

    print("The Dial starts by pointing at " + initial_number)
    for r in combinations:
        if rotate_dial(r):
            global password
            password += 1

    print("Password: ", password)


if __name__ == "__main__":
    main()

