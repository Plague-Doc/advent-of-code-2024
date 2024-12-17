# https://adventofcode.com/2024/day/2
INPUTS = "inputs/day_2.txt"

def one_star():
    with open(INPUTS, "r") as file:
        data = [list(map(int, line.split())) for line in file]
    
    safe_reports = 0

    for report in data:
        if sorted(report) != report and sorted(report, reverse = True) != report:
            continue

        differences = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
        if max(differences) > 3 or min(differences) < 1:
            continue

        safe_reports += 1

    return safe_reports

def two_star():
    with open(INPUTS, "r") as file:
        data = [list(map(int, line.split())) for line in file]
    
    safe_reports = 0

    def valid_order(arr):
        return sorted(arr) == arr or sorted(arr, reverse = True) == arr

    def valid_deviation(arr):
        differences = [abs(arr[i + 1] - arr[i]) for i in range(len(arr) - 1)]
        return max(differences) <= 3 and min(differences) >= 1

    for report in data:
        if valid_order(report) and valid_deviation(report):
            safe_reports += 1
            continue
        
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:]
            if valid_order(modified_report) and valid_deviation(modified_report):
                safe_reports += 1
                break

    return safe_reports

if __name__ == "__main__":
    print("One star solution:", one_star())
    print("Two star solution:", two_star())
