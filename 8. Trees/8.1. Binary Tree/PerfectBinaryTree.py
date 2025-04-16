"""
A perfect binary tree is a type of tree 
where the leaf nodes are at equal depth

         1
       /   \
      2     3
     / \   / \
    4   5 6   7

Represented as an array

"""

from BinaryTree import BinaryTree
from Node import Node


nodes = [Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)]

for i in range(len(nodes) // 2):
    nodes[i].left = nodes[2*i+1]
    nodes[i].right = nodes[2*i+2]