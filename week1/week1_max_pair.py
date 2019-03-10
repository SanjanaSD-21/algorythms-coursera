# python3


def max_pairwise_product(numbers):
    first_num = 0
    second_num = 0
    n = len(numbers)
    for index_num in range(n):
        if numbers[index_num] > first_num:
            second_num = first_num
            first_num = numbers[index_num]
        elif numbers[index_num] > second_num:
            second_num = numbers[index_num]
    return first_num * second_num


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))