#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,

# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# tree = { node1: { label1: c1, label2: c2, ...}, node2, ... }
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


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
