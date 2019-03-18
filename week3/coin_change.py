# Uses python3
import sys


def get_change(m):
    if m == 10 or m == 5 or m == 1:
        return 1
    elif m > 10:
        return int(m/10) + get_change(int(m % 10))
    elif m > 5:
        return int(m/5) + get_change(int(m % 5))
    else:
        return m


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
