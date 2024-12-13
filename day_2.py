# https://adventofcode.com/2024/day/2

def one_star():
    with open("day_2.txt", "r") as file:
        data = [list(map(int, line.split())) for line in file]
    
    safe_reports = 0
    for report in data:
        if len(report) < 2:
            continue

        if sorted(report) != report and sorted(report, reverse = True) != report:
            continue

        differences = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
        if max(differences) > 3 or min(differences) < 1:
            continue

        safe_reports += 1

    return safe_reports

def two_star():
    pass

if __name__ == "__main__":
    print("One star solution:", one_star())
    print("Two star solution:", two_star())
