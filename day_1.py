# https://adventofcode.com/2024/day/1

def one_star():
    with open("day_1.txt", "r") as file:
        data = [line.split() for line in file]

    list_a = sorted(int(x[0]) for x in data)
    list_b = sorted(int(x[1]) for x in data)
    
    return sum(abs(a - b) for a, b in zip(list_a, list_b))

def two_star():
    with open("day_1.txt", "r") as file:
        data = [line.split() for line in file]
    
    list_a = [int(x[0]) for x in data]
    list_b = [int(x[1]) for x in data]

    return sum((x * list_b.count(x)) for x in list_a)

if __name__ == "__main__":
    print("One star solution:", one_star())
    print("Two star solution:", two_star())
