# Uses python3
import sys


def get_change(m):

    if m == 2:
        return 2
    leftover = m % 4
    if leftover == 0:
        return int(m / 4)

    return int(m/4)+1


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    # for i in range(1, 40):
    #     print(" current value: " + str(i) + " coins needed: " + str(get_change(i)))
