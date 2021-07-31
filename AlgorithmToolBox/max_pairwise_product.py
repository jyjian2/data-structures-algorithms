# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    i = 0
    j = 0
    max1 = 0
    max2 = 0

    while i < n:
        if numbers[i] > max1:
            max1 = numbers[i]
            max1_index = i
        i += 1

    while j < n:
        if numbers[j] > max2 and j != max1_index:
            max2 = numbers[j]
        j += 1

    return max1 * max2




if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
