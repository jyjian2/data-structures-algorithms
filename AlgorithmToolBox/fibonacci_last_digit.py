# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if (n <= 1):
        return n
    else:
        a = []
        a.append(0)
        a.append(1)

        for i in range(2, n+1):
            a.append((a[i-1]+a[i-2])%10)

        return a[n]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
