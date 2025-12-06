
def read_input(filename: str) -> str: 
    try:
        with open(filename) as f:
            return f.readline()
    except FileNotFoundError:
        return ""
    
def clean_text (string: str) -> str:
    return string.replace("\n","")


def check(product_ranges: str) -> int:    
    '''
    Identify all the invalid IDs appear in the given ranges,
    returns the sum of all the invalid IDs
    '''
    result = 0

    # get the list of each range in ranges, separated by comma
    ranges = product_ranges.split(",")
    for range in ranges:
        result += find_invalid_ids(range)
    
    return result


def find_invalid_ids(id_range: str) -> int:
    '''
    returns the sum of the invalid ids of the given range

    Invalid IDs:
    - no leading 0
    - sequence of digits repeated twice
    '''
    invalid_ids = 0
    a,b = id_range.split("-")
    for id in range(int(a),int(b)+1):
        if has_leading_zero(id) or is_sequence_of_digits(id):
            #print(id)
            invalid_ids += id 

    return invalid_ids

def has_leading_zero(n:int) -> bool:
    return str(n)[0] == "0"

def is_sequence_of_digits(n:int) -> bool:
    '''
    Return true if the number is a sequence of digits repeated ONLY twice
    '''
    id_str = str(n)
    id_len = len(id_str)

    if id_len % 2 == 0:
        return id_str[0:(id_len//2)] == id_str[(id_len)//2:]
    return False

def main():
    ranges = read_input("gift_shop_input.txt")
    print(check(ranges))

if __name__ == "__main__":
    main()