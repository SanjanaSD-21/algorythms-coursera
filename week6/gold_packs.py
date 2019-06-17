# Uses python3
import sys


def optimal_weight(weight_limit, items):
    # write your code here
    len_items = len(items) + 1
    len_limits = weight_limit + 1
    capacity = [[0 for i in range(0, len_limits)] for j in range(0, len_items)]
    for i in range(1, len_items):
        for w in range(1, len_limits):
            capacity[i][w] = capacity[i-1][w]
            if items[i-1] <= w:
                val = capacity[i - 1][w - items[i-1]] + items[i-1]
                if capacity[i][w] < val:
                    capacity[i][w] = val
    return capacity[len_items-1][len_limits-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
