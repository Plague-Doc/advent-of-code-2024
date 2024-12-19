# https://adventofcode.com/2024/day/5
INPUTS = "inputs/day_5.txt"

def one_star():
    with open(INPUTS, "r") as file:
        data = [line.strip() for line in file]

    rules = [
        tuple(map(int, rule.split('|')))
        for rule in data[:data.index('')]]
    
    pages = [
        list(map(int, page.split(',')))
        for page in data[data.index('') + 1:]]
    
    def valid_pos(page, page_num):
        for a, b in rules:
            if a == page_num and b in page:
                if page.index(page_num) > page.index(b):
                    return False
            elif b == page_num and a in page:
                if page.index(page_num) < page.index(a):
                    return False
        return True
    
    total = 0
    for page in pages:
        if all(valid_pos(page, num) for num in page):
            total += page[len(page) // 2]
    
    return total

def two_star():
    pass

if __name__ == "__main__":
    print("One star solution:", one_star())
    print("Two star solution:", two_star())
