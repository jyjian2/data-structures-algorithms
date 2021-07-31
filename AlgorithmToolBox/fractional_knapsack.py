# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    lst = []
    n = len(weights)
    for i in range(n):
        lst.append((values[i], weights[i]))

    lst.sort(key=lambda x: x[0]/x[1], reverse = True)

    total_value = 0
    i = 0

    while capacity > 0 and i < n:
        if capacity >= lst[i][1]:
            total_value += lst[i][0]
            capacity -= lst[i][1]
        else:
             total_value += lst[i][0]/lst[i][1]*capacity
             capacity = 0
        i += 1
    return total_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
