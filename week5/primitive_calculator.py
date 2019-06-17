# Uses python3
import sys


def gen_seq(n):
    seq = [0] * (n + 1)
    seq[1] = 1
    for i in range(2, n+1):
        temp = i - 1
        if i % 2 == 0:
            rem = i // 2
            if seq[temp] > seq[rem]:
                temp = rem
        if i % 3 == 0:
            rem = i // 3
            if seq[temp] > seq[rem]:
                temp = rem
        seq[i] = seq[temp] + 1

    return seq


def optimal_sequence(n):
    generated = gen_seq(n)
    index = n
    # print(generated)
    sequence = [index]
    while index > 1:
        temp = index - 1
        if index % 2 == 0:
            rem = index // 2
            if generated[temp] > generated[rem]:
                temp = rem
        if index % 3 == 0:
            rem = index // 3
            if generated[temp] > generated[index//3]:
                temp = rem

        index = temp
        sequence.append(index)

    last_elem_index = len(sequence)-1
    print(last_elem_index)
    for x in range(last_elem_index, -1, -1):
        print(sequence[x], end=' ')


input = sys.stdin.read()
n = int(input)
optimal_sequence(n)
# print(len(sequence) - 1)
# for x in sequence:
#     print(x, end=' ')