# python3
import sys

def InverseBWT(bwt):
    bwt_order = []
    d = {'$': 0, 'A': 0, 'C': 0, 'G': 0, 'T': 0 }
    for i in bwt:
        d[i] += 1
        bwt_order.append((i, d[i]))

    acc = 0
    for s in ['$', 'A', 'C', 'G', 'T']:
        count = d[s]
        d[s] = acc
        acc += count

    # print(d)
    # print((bwt_order))
    # print(len(bwt_order))

    cur = 0
    res = ['$']
    for i in range(len(bwt_order) - 1):
        t = bwt_order[cur]
        res.append(t[0])
        cur = d[t[0]] + t[1] - 1
    res.reverse()
    return "".join(res)

if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
