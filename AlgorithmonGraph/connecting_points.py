#Uses python3
import sys
import math
import heapq


def find(sets, v):
    for i, s in enumerate(sets):
        if v in s:
            return i
    return -1 # BUG

def minimum_distance(x, y):
    result = 0
    sets = []
    for i in range(len(x)):
        s = set()
        s.add(i)
        sets.append(s)

    edges = []
    for i in range(len(x)):
        for j in range(i + 1, len(y)):
            # print(i, j)
            d = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            heapq.heappush(edges, (d, i, j))
    
    while len(edges) > 0:
        d, v1, v2 = heapq.heappop(edges)
        s1 = find(sets, v1)
        s2 = find(sets, v2)
        if s1 != s2:
            result += d
            sets[s1] |= sets[s2]
            sets.pop(s2)
    return result

    #
    # #create an array to store all edges
    # edges = [[0 for i in range(len(x))] for j in range(len(y))]
    # for i in range(len(x)):
    #     for j in range(len(y)):
    #         weight = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** .5
    #         edges[i][j] = weight



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
