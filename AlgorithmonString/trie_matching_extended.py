# python3
import sys

def build_trie(patterns):
    tree = dict()
    node = 0
    for pattern in patterns:
        i = 0
        for idx, letter in enumerate(pattern):
            is_leaf = idx == (len(pattern) - 1)
            if tree.get(i):
                if letter not in tree[i]:
                    tree[i].update({letter: (node + 1, is_leaf)})
                    node += 1
                    i = node
                else:
                    # is_leaf = is_leaf or tree[i][letter][1]
                    n, old_is_leaf = tree[i][letter]
                    is_leaf |= old_is_leaf
                    tree[i][letter] = (n, is_leaf)
                    i = n
            else:
                tree[i] = {letter: (node + 1, is_leaf)}
                node += 1
                i = node
    return tree

def prefix_trie_matching(text, trie):
    n = 0
    for s in text:
        if s in trie[n]:
            n, is_leaf = trie[n][s]
            if is_leaf:
                return True
        else:
            return False
    return False

def trie_matching(text, trie):
    res = []
    for i in range(len(text)):
        r = prefix_trie_matching(text[i:], trie)
        if r:
            res.append(i)
    return res

def solve (text, n, patterns):
    trie = build_trie(patterns)
    return trie_matching(text,trie)

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
