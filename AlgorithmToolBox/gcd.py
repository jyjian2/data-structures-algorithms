# Uses python3
import sys

def gcd_naive(a, b):
    if a < b:
        temp = a
        a = b
        b = temp

    while b!=0:
            aprime = a % b
            a = b
            b = aprime

    current_gcd = a

    return current_gcd

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
