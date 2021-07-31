# python3
def siftDown(i, results, data):
    size = len(data) - 1

    minIndex = i
    left = 2 * i
    if left <= size and data[left] < data[minIndex]:
        minIndex = left
    right = (2 * i) + 1
    if right <= size and data[right] < data[minIndex]:
        minIndex = right
    if i != minIndex:
        #store index of swap in the array swaps
        result = (i - 1, minIndex - 1)
        results.append(result)
        #swap data[i] and data[minIndex]
        temp = data[i]
        data[i] = data[minIndex]
        data[minIndex] = temp
        siftDown(minIndex, results, data)


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    data.insert(0, 0)
    results = []
    for i in range((len(data) - 1) // 2, 0, -1):
        siftDown(i, results, data)
    return results


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n


    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
