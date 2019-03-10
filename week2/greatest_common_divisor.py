# Uses python3
import sys
import math

def gcd_naive(a, b):
    if a == b:
        return a
    lower_value = min(a, b)
    greater_value = max(a, b)

    end_point = int(math.sqrt(lower_value)) + 1
    temp_res = 1
    for d in range(2, end_point, 1):
        result = int(lower_value / d)
        if lower_value % d == 0:
            if greater_value % result == 0:
                return result
            elif greater_value % d == 0:
                temp_res = d
    return temp_res

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))