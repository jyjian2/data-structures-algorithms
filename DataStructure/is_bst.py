#!/usr/bin/python3

import sys, threading
#
sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def inorderTraverse(tree, nodeIndex, floor, ceiling):
    if nodeIndex == -1:
        return True
    nodeVal = tree[nodeIndex][0]
    leftIndex = tree[nodeIndex][1]
    rightIndex = tree[nodeIndex][2]

    if nodeVal <= floor or nodeVal >= ceiling:
        return False

    return inorderTraverse(tree, leftIndex, floor, nodeVal) and \
            inorderTraverse(tree, rightIndex, nodeVal, ceiling)


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  if len(tree) == 0:
      return True
  return inorderTraverse(tree, 0, -(1<<31), (1<<31)-1)


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
