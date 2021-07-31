# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inordernested(self, x):
    if x != -1:
            # print(x)
        self.inordernested(self.left[x])
        self.result.append(self.key[x])
        self.inordernested(self.right[x])

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    #left->key->right
    x = 0
    self.inordernested(x)
    return self.result

  def preordernested(self, x):
    if x != -1:
        self.result.append(self.key[x])
        self.preordernested(self.left[x])
        self.preordernested(self.right[x])

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    x = 0
    self.preordernested(x)
    return self.result

  def postordernested(self, x):
      if x != -1:
       self.postordernested(self.left[x])
       self.postordernested(self.right[x])
       self.result.append(self.key[x])

  def postOrder(self):
    x = 0
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self.postordernested(x)
    return self.result

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
