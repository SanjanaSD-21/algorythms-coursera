# python3
import sys


def compute_min_refills(distance, tank, stops):
    if distance <= tank:
        return 0
    starting_point = 0
    refuels = 0
    # write your code here
    for i in range(len(stops)):
        hasStop = False
        while stops[i] - starting_point <= tank:
            i += 1
            hasStop = True
            if i == len(stops):
                break
        if hasStop:
            starting_point = stops[i-1]
            refuels += 1
            if starting_point + tank >= distance:
                return refuels
        else:
            return -1
    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
