"""
A degenerate binary tree 
is a binary tree that each node has a maximum of 1 single child

        1
       /
      2
     /
    3
     \
      4
     /
    5
"""

from Node import Node

root = Node(1)
root.left = Node(2)
root.left.left = Node(3)
root.left.left.right = Node(4)
root.left.left.right.left = Node(5)