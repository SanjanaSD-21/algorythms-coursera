# Uses python3
import sys
import itertools


def is_partitionable(one_third, sum_a, sum_b, sum_c, items):
    remaining_items = len(items)
    if remaining_items == 0:
        if sum_a == sum_b and sum_b == sum_c:
            return True
        else:
            return False
    elif one_third == sum_c and sum_c == sum_b and sum_b == sum_a:
        return False

    if sum_a > one_third or sum_b > one_third or sum_c > one_third:
        return 0

    new_items = items.copy()
    next_elem = new_items.pop(0)
    if sum_a == one_third:
        if sum_b == one_third:
            return is_partitionable(one_third, sum_a, sum_b, sum_c + next_elem, new_items)
        else:
            return is_partitionable(one_third, sum_a, sum_b + next_elem, sum_c, new_items) or \
                   is_partitionable(one_third, sum_a, sum_b, sum_c + next_elem, new_items)
    elif sum_b == one_third:
        if sum_c == one_third:
            return is_partitionable(one_third, sum_a + next_elem, sum_b, sum_c, new_items)
        else:
            return is_partitionable(one_third, sum_a + next_elem, sum_b, sum_c, new_items) or \
                   is_partitionable(one_third, sum_a, sum_b, sum_c + next_elem, new_items)
    elif sum_c == one_third:
        return is_partitionable(one_third, sum_a + next_elem, sum_b, sum_c, new_items) or \
               is_partitionable(one_third, sum_a, sum_b + next_elem, sum_c, new_items)
    else:
        return is_partitionable(one_third, sum_a + next_elem, sum_b, sum_c, new_items) \
               or is_partitionable(one_third, sum_a, sum_b + next_elem, sum_c, new_items) \
               or is_partitionable(one_third, sum_a, sum_b, sum_c + next_elem, new_items)


def partition3(items):
    number_of_items = len(items)
    if number_of_items < 3:
        return 0

    total_sum = sum(items)
    if total_sum % 3 != 0:
        return 0

    max_elem = max(items)
    one_third = int(total_sum / 3)
    if max_elem > one_third:
        return 0

    if is_partitionable(one_third, 0, 0, 0, items):
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))
