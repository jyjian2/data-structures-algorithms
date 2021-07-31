# Uses python3
#import sys

"""def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))"""

import sys

def lcm_naive(a, b):

    c = find_gcd(a, b)

    return a*b // c


def find_gcd(a, b):
    if a < b:
        temp = a
        a = b
        b = temp

    while b!=0:
            aprime = a % b
            a = b
            b = aprime

    return a

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
