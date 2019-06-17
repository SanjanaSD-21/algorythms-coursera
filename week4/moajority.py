# Uses python3
import sys


def get_majority_element(a, arr_length):
    if 1 == arr_length:
        return a[0]
    if 2 == arr_length:
        if a[0] == a[1]:
            return a[0]
        else:
            return -1

    a.sort()
    median = int(arr_length / 2)
    if a[median] == a[0]:
        return 0
    counter = 0
    threshold = median + 1
    for i in range(0, arr_length):
        if a[median] == a[i]:
            counter += 1
        if threshold == counter:
            return 0
    return -1



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, n) != -1:
        print(1)
    else:
        print(0)
