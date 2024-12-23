# https://adventofcode.com/2024/day/6
INPUTS = "inputs/day_6.txt"

def one_star():
    with open(INPUTS, "r") as file:
        data = [line.strip() for line in file]
    
    start_line = next((i for i, sublist in enumerate(data) if '^' in sublist))
    pos = (start_line, data[start_line].index('^'))
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    turn = 0

    while 0 <= pos[0] < len(data) and 0 <= pos[1] < len(data[0]):
        data[pos[0]] = data[pos[0]][:pos[1]] + 'X' + data[pos[0]][pos[1] + 1:]
        
        if data[pos[0] + dir[turn][0]][pos[1] + dir[turn][1]] == '#':
            turn = turn + 1 if turn < len(dir) - 1 else 0
        else:
            pos = (pos[0] + dir[turn][0], pos[1] + dir[turn][1])
    
    return sum(line.count('X') for line in data)

def two_star():
    pass

if __name__ == "__main__":
    print("One star solution:", one_star())
    print("Two star solution:", two_star())
