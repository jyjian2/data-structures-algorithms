#Uses python3

import sys

def dfs(adj, visited, v):
    visited[v] = True
    result = []
    for next in adj[v]:
        if not visited[next]:
            result.append(dfs(adj, visited, next))
        else:
            return True
    visited[v] = False
    return True in result



def acyclic(adj):
    visited = [False] * len(adj)
    for i in range(len(adj)):
        if dfs(adj, visited, i):
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
