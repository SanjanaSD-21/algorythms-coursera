# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n < 2:
        return n
    num1 = 1
    num2 = 2
    counter = 1
    while num1 != 1 or num2 != 1:
        temp = num1 + num2
        num1 = num2
        num2 = temp % m
        counter += 1
    desired_index = n % counter
    if desired_index < 2:
        return desired_index
    elif desired_index == 2:
        return 1

    first_val = 1
    second_val = 1
    for i in range(2, counter+1):
        temp = first_val
        first_val += second_val
        first_val %= m
        if i == desired_index - 1:
            return first_val
        second_val = temp


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))