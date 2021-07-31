
# Uses python3
import sys
import itertools


def solution(arr):
    import numpy as np
    total = sum(arr)
    if len(arr) < 3 or total % 3:
        return 0
    per_person = total // 3
    dp = np.zeros((per_person+1,len(arr)+1))

    for i in range(1, per_person+1):
        for j in range(1, len(arr)+1):
            ii = i - arr[j - 1]
            if arr[j - 1] == i or (ii > 0 and dp[ii][j - 1]):

                dp[i][j] = 1 if dp[i][j - 1] == 0 else 2

            else:
                dp[i][j] = dp[i][j - 1]

    return 1 if dp[-1][-1] == 2 else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
#     print(partition3(A))
    print(solution(A))
