# Uses python3
import sys

def optimal_weight(W, w):

    n = len(w)

    w.insert(0, 0)

    #create a two way arrays
    value = [[0] * (W + 1) for e in range(n + 1)]
    #initialize the array
    for item in range(n + 1):
        value[item][0] = 0
    for capacity in range(W + 1):
        value[0][capacity] = 0

    for i in range(1, n + 1):
        for c in range(1, W + 1):
            value[i][c] = value[i - 1][c]
            if w[i] <= c:
                val = value[i - 1][c - w[i]] + w[i]
                if value[i][c] < val:
                    value[i][c] = val

    return value[n][W]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
