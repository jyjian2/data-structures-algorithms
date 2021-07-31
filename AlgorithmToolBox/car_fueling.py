# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.insert(0, 0)
    stops.append(distance)
    n = len(stops)
    i = 0
    drove = 0
    time = 0


    while i < n - 1:
        s = stops[i]
        ns = stops[i+1]
        if ns - s > tank:
            return -1

        elif drove + ns - s <= tank:
            drove += ns - s
            i += 1

        else:
            time += 1
            drove = 0


    return time

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
