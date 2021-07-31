# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, n):
        self.value = n
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

                self.nodes = []
                for i in range(self.n):
                    self.nodes.append(Node(i))

                for c in range(self.n):
                    p = self.parent[c]
                    # print("adding child {} to parent {}".format(int(c), int(p)))
                    if p == -1:
                        self.root = c
                        continue
                    self.nodes[p].add_child(c)

                # for n in self.nodes:
                #     print(n.value, n.children)


        def compute_height(self):
                queue = []
                queue.append(self.root)

                while len(queue) > 0:
                    node = queue.pop(0)
                    children = self.nodes[node].children
                    # print("node is {} adding children {}".format(str(node), str(children)))
                    for c in children:
                        queue.append(c)
                # Replace this code with a faster implementation
                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;


def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
