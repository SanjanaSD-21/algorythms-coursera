# Uses python3
import sys
import random


def partition3(a, left_index, right_index):
    if right_index - left_index == 1:
        if a[left_index] > a[right_index]:
            a[left_index], a[right_index] = a[right_index], a[left_index]
        return [right_index, right_index]
    pivot_element = a[left_index]
    index_lower = left_index
    index_greater = right_index

    for index in range(left_index, right_index+1):
        if index > index_greater or index_lower >= index_greater:
            break
        if pivot_element == a[index]:
            continue

        should_exit = False
        while pivot_element < a[index]:
            a[index], a[index_greater] = a[index_greater], a[index]
            index_greater -= 1
            if index == index_greater:
                should_exit = True
                break

        while pivot_element > a[index]:
            a[index], a[index_lower] = a[index_lower], a[index]
            index_lower += 1

        if should_exit:
            break

    new_right = right_index
    if index_greater < right_index:
        new_right = index_greater

    if index_greater != index_lower:
        new_right -= 1

    new_left = left_index
    if index_lower > left_index:
        new_left = index_lower

    return [new_left, new_right]


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, left_index, right_index):
    if left_index >= right_index:
        return
    k = random.randint(left_index, right_index)
    # k = left_index
    a[left_index], a[k] = a[k], a[left_index]
    #use partition3
    # m = partition2(a, left_index, right_index)
    # randomized_quick_sort(a, left_index, m - 1);
    # randomized_quick_sort(a, m + 1, right_index);

    arr_parts = partition3(a, left_index, right_index)
    randomized_quick_sort(a, left_index, arr_parts[0] - 1)
    randomized_quick_sort(a, arr_parts[1] + 1, right_index)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
