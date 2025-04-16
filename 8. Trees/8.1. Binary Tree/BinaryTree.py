"""

    1
   / \
  2   4
   \
    3

"""

from Node import Node

root = Node(1)
root.left = Node(2)
root.left.right = Node(3)

root.right = Node(4)

class BinaryTree:
    def __init__(self, nodes):
        self.root = Node(nodes[0])
        current = self.root
        
        i = 1
        while i < len(nodes):
            current.left = Node(nodes[i])
            i += 1
            current.right = Node(nodes[i])

    def buildTree(self, root, nodes, i = 0):
        root = Node(nodes[i])
        i += 1
        self.buildTree(root.left, nodes, i)
        i += 1
        self.buildTree(root.right, nodes, i)

    def print(self, root):
        print(root.data, end=" ")
        if root.left:
            self.print(root.left, end=" ")
        if root.right:
            self.print(root.right, end=" ")


