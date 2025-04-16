"""
A complete binary tree is a tree
where all levels of the tree are filled
completely except the lowest level nodes
which are filled from as left as possible
     A
   /   \
  B     C
 / \   /
D   E F
"""

from Node import Node

root = Node('A')

root.left = Node('B')
root.left.left = Node('D')
root.left.right = Node('E')

root.right = Node('C')
root.right.left = Node('F')
