

def read_input(filename: str) -> str: 
    try:
        with open(filename) as f:
            return f.readlines()
    except FileNotFoundError:
        return ""
    
def clean_text (string: str) -> str:
    return string.replace("\n","")


def tot_output(banks: list[str]) -> int:
    '''
    find the largest possibile joltage a bank can produce
    '''
    total = 0
    for bank in banks:
        #print(bank_joltage(bank))
        total += int(bank_joltage(bank))

    return total

def bank_joltage(bank: str):
    # find the first max and its index
    # 1. if the first max index is the last element of the array -> find the second max in the subarray [0-len(arr)-1]
    # 2. if the first max index is NOT the last element of the array -> find the second max in the subarray [first_max_index+1 - len(arr)-1]
    # 3. combine the two elements found based on their index order. Return the element

    first_max = find_max(bank,0,len(bank))
    second_max = None

    if first_max["index"] == len(bank)-1:
        second_max = find_max(bank,0,len(bank)-1)
    else:
        second_max = find_max(bank,first_max["index"]+1,len(bank))

    # combine elements
    if first_max["index"] < second_max["index"]:
        return first_max["value"] + second_max["value"]
    return second_max["value"] + first_max["value"]

def find_max(arr:str,start:int,end:int):
    '''
    return the max element and its index
    '''
    max_index = start
    max_elem = arr[max_index]

    for i in range(start+1,end):
        if int(arr[i]) > int(max_elem):
            max_elem = arr[i]
            max_index = i
    
    return {"index":max_index,"value":max_elem}


def main():
    banks = list(map(clean_text,read_input("lobby_input.txt")))
    print("total joltage: ", tot_output(banks))

if __name__ == "__main__":
    main()