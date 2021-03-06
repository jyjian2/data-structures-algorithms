#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    dist = [-1] * len(adj)
    prev = [-1] * len(adj)

    dist[0] = 0
    for i in range(len(adj)):
        for j in range(len(adj)):
            for ind, k in enumerate(adj[j]):
                jkCost = cost[j][ind]
                if dist[k] > dist[j] + jkCost:
                    dist[k] = dist[j] + jkCost
                    prev[k] = j
        if i == len(adj) - 2:
            dist_vminus1 = list(dist)
        if i == len(adj) - 1:
            dist_v = list(dist)
    if dist_vminus1 == dist_v:
        return 0
    else:
        return 1
        
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
