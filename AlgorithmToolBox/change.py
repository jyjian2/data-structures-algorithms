# Uses python3
import sys

def get_change(m):
    sum = 0
    #write your code here
    #Deal with 10
    sum += m // 10
    m = m % 10

    sum += m // 5
    m = m % 5

    sum += m

    return sum

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
