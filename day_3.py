import re

# https://adventofcode.com/2024/day/3
INPUTS = "inputs/day_3.txt"

def one_star():
    with open(INPUTS, "r") as file:
        data = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", file.read())
        
    return sum(int(a) * int(b) for a, b in data)

def two_star():
    with open(INPUTS, "r") as file:
        data = re.findall(r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)", file.read())
    
    total = 0
    count_mults = True

    for element in data:
        if element == "do()":
            count_mults = True
        elif element == "don't()":
            count_mults = False
        elif count_mults:
            nums = re.findall(r"\d+", element)
            total += int(nums[0]) * int(nums[1])
    
    return total

if __name__ == "__main__":
    print("One star solution:", one_star())
    print("Two star solution:", two_star())
