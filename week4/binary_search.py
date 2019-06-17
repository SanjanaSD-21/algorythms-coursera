# Uses python3
import sys


def optimised_binary(left, right, a, x):
    while left != right:
        if a[left] > x:
            return -1
        if a[right] < x:
            return -1
        elem_to_check = left + int((right - left) / 2)
        if a[elem_to_check] == x:
            return elem_to_check
        elif a[elem_to_check] < x:
            left = elem_to_check + 1
        else:
            right = elem_to_check - 1

    if a[left] == x:
        return left
    else:
        return -1


def binary_search(current_counter, a, x):
    length_a = len(a)
    if length_a == 0:
        return -1
    if length_a == 1:
        if a[0] == x:
            return current_counter
        else:
            return -1
    if a[0] > x:
        return -1
    if a[length_a-1] < x:
        return -1
    if length_a == 2:
        if a[0] == x:
            return current_counter
        elif a[1] == x:
            return current_counter+1
        else:
            return -1
    if length_a == 3:
        if a[0] == x:
            return current_counter
        elif a[1] == x:
            return current_counter+1
        elif a[2] == x:
            return current_counter+2
        else:
            return -1

    elem_to_check = int(length_a / 2)
    if a[elem_to_check] == x:
        return current_counter + elem_to_check
    elif a[elem_to_check] < x:
        return binary_search(current_counter + elem_to_check+1, a[elem_to_check:length_a], x)
    else:
        return binary_search(current_counter, a[0:elem_to_check], x)



def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #print(binary_search(0, a, x), end = ' ')
        print(optimised_binary(0, len(a)-1, a, x), end = ' ')
#        print(linear_search(a, x), end = ' ')