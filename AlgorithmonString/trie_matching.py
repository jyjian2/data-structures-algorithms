# python3
import sys

def build_trie(patterns):
    tree = dict()
    node = 0
    for pattern in patterns:
        i = 0
        for letter in pattern:
            if tree.get(i):
                if letter not in tree[i]:
                    tree[i].update({letter: node + 1})
                    node += 1
                    i = node
                else:
                    i = tree[i][letter]
            else:
                tree[i] = {letter: node + 1}
                node += 1
                i += 1
    return tree

def prefix_trie_matching(text, trie):
    # i is the first letter in target text
    # v (node) is the root of trie
    i = 0
    v = 0
    while 1:
        # leaf node won't have edge so it's not in the trie
        # tree = { node1: { label1: c1, label2: c2, ...}, node2, ... }
        # e.g. {0:{'A':1,'T':2},1:{'C':3}}
        if v not in trie:
            return True
        if i >= len(text):
            return False
        s = text[i]
        #
        if s in trie[v]:
            v = trie[v][s]
            i += 1
        else:
            return False

def trie_matching(text, trie):
    res = []
    for i in range(len(text)):
        r = prefix_trie_matching(text[i:], trie)
        # print(i, r)
        if r:
            res.append(i)
    return res

def solve (text, n, patterns):
    trie = build_trie(patterns)
    return trie_matching(text,trie)


text = sys.stdin.readline().strip()
n = int (sys.stdin.readline().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
