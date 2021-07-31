# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    min_num_coins = [0] * (m+1)

    if m == 0:
        return 0

    for amount in range(1, m + 1):
        min_num_coins[amount] = m + 1
        for i in range(len(coins)):
            if amount >= coins[i]:
                num_coins = min_num_coins[amount - coins[i]] + 1
                if num_coins < min_num_coins[amount]:
                    min_num_coins[amount] = num_coins

    return min_num_coins[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    # 1 3 4
