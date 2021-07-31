# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []

    # add each segment as an element of tuple
    # Each element has segment's start and end point
    # print(segments)
    for s in segments:
        points.append((s.start, s.end))

    points.sort(key=lambda x: x[1])

    base_index = 0
    compare_index = 0
    count = 0
    visits = []

    while base_index < len(points):
        compare_index = base_index + 1
        while compare_index < len(points) and points[base_index][1] >= points[compare_index][0]:
            compare_index += 1
        count += 1
        visits.append(points[base_index][1])
        base_index = compare_index

    print(count)
    # first variable = index, second = the value of index
    for i, v in enumerate(visits):
        if i == 0:
            print(v, end = "")
        else:
            print(" " + str(v), end = "")
    print("")




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
