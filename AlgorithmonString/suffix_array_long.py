# python3
import sys

def count_sort(s):
    order = [0] * len(s)
    count = [0] * 5
    for i, c in enumerate(s):
        if c == '$':
            count[0] += 1
        if c == 'A':
            count[1] += 1
        if c == 'C':
            count[2] += 1
        if c == 'G':
            count[3] += 1
        if c == 'T':
            count[4] += 1
    for i, c in enumerate(count):
        if i == 0:
            continue
        count[i] += count[i-1]
    for i in range(len(s)-1, -1, -1):
        c = s[i]
        if c == '$':
            count[0] -= 1
            order[count[0]] = i
        if c == 'A':
            count[1] -= 1
            order[count[1]] = i
        if c == 'C':
            count[2] -= 1
            order[count[2]] = i
        if c == 'G':
            count[3] -= 1
            order[count[3]] = i
        if c == 'T':
            count[4] -= 1
            order[count[4]] = i
    return order

def build_char_classes(s, order):
    classes = [0] * len(s)
    for i in range(1, len(s)):
        if s[order[i]] != s[order[i-1]]:
            classes[order[i]] = classes[order[i-1]] + 1
        else:
            classes[order[i]] = classes[order[i-1]]
    return classes

def sort_douled(s, l, order, classes):
    count = [0] * len(s)
    new_order = [0] * len(s)
    for i in range(len(s)):
        count[classes[i]] += 1
    for i in range(1, len(s)):
        count[i] += count[i-1]
    for i in range(len(s) - 1, -1, -1):
        start = (order[i] - l + len(s)) % len(s)
        cl = classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order

def update_classes(new_order, classes, l):
    n = len(new_order)
    new_classes = [0] * n
    for i in range(1, n):
        cur = new_order[i]
        prev = new_order[i-1]
        mid = cur + l
        mid_prev = (prev + l) % n
        if classes[cur] != classes[prev] or classes[mid] != classes[mid_prev]:
            new_classes[cur] = new_classes[prev] + 1
        else:
            new_classes[cur] = new_classes[prev]
    return new_classes


def build_suffix_array(text):
    """
    Build suffix array of the string text and
  return a list result of the same length as the text
  such that the value result[i] is the index (0-based)
  in text where the i-th lexicographically smallest
  suffix of text starts.
    """
    result = []
    order = count_sort(text)
    classes = build_char_classes(text, order)
    l = 1
    while l < len(text):
        order = sort_douled(text, l, order ,classes)
        classes = update_classes(order, classes, l)
        l *= 2
    for i in range(len(order)):
        order[i] = (order[i] + len(text)) % len(text)
    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
