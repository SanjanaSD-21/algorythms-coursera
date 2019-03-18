# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # sort weights and values
    limit = capacity
    if limit == 0:
        return 0.

    valuePerWeight = sorted([[v / w, w] for v, w in zip(values, weights)], reverse=True)
    for index, itemWeight in enumerate(valuePerWeight):
        if limit <= 0:
            break
        elif itemWeight[1] > limit:
            return value + limit * itemWeight[0]
        else:
            limit -= itemWeight[1]
            value += itemWeight[1] * itemWeight[0]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
