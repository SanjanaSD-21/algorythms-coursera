# Uses python3


def next_char(ch, string, starting_index):
    for i in range(starting_index, len(string)):
        if string[i] == ch:
            return i
    return -1


def edit_distance(s1, s2):
    # write your code here. Levenshtein
    len_s1 = len(s1) + 1
    len_s2 = len(s2) + 1

    # init 0 matrix
    dist = [[0 for i in range(0, len_s2)] for j in range(0, len_s1)]

    # set first row
    for i in range(1, len_s1):
        dist[i][0] = i

    for i in range(1, len_s2):
        dist[0][i] = i

    for j in range(1, len_s2):
        for i in range(1, len_s1):
            cost = 1
            if s1[i-1] == s2[j-1]:
                cost = 0
            dist[i][j] = min( dist[i-1][j] + 1,         # remove
                              dist[i][j-1] + 1,         # insert
                              dist[i-1][j-1] + cost)    # exchange

    return dist[len_s1-1][len_s2-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
