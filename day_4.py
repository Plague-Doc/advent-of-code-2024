# https://adventofcode.com/2024/day/4
INPUTS = "inputs/day_4.txt"

def one_star():
    SEARCH_WORD = "XMAS"
    with open(INPUTS, "r") as file:
        data = [line.strip() for line in file]

    total_words = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def search(i, j, id, jd):
        if not (0 <= i + (len(SEARCH_WORD) - 1) * id < len(data) and
                0 <= j + (len(SEARCH_WORD) - 1) * jd < len(data[0])):
            return None
        
        return "".join(data[i + k * id][j + k * jd] for k in range(len(SEARCH_WORD)))
        
    for i in range(len(data)):
        for j in range(len(data[i])):
            for id, jd in directions:
                if search(i, j, id, jd) == SEARCH_WORD:
                    total_words += 1
    
    return total_words

def two_star():
    SEARCH_WORD = "MAS"
    with open(INPUTS, "r") as file:
        data = [line.strip() for line in file]

    total_words = 0
    directions = [(-1, -1, 1, 1), (-1, 1, 1, -1), (1, -1, -1, 1), (1, 1, -1, -1)]

    def search(i, j):
        words = [data[i + s1][j + s2] + 'A' + data[i + e1][j + e2] for s1, s2, e1, e2 in directions]
        return words.count(SEARCH_WORD) == 2

    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            if data[i][j] == 'A' and search(i, j):
                total_words += 1
    
    return total_words

if __name__ == "__main__":
    print("One star solution:", one_star())
    print("Two star solution:", two_star())
