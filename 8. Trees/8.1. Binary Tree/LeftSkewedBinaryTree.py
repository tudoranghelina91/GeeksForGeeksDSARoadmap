from Node import Node
"""
        1
       /
      2
     /
    3
   /
  4
 /
5
"""
root = Node(1)
root.left.left = Node(2)
root.left.left.left = Node(3)
root.left.left.left.left = Node(4)
root.left.left.left.left.left = Node(5)