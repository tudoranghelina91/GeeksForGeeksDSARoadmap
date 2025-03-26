from Node import Node
"""
        1
         \
          2
           \
            3
             \
              4
               \
                5
"""
root = Node(1)
root.right.right = Node(2)
root.right.right.right = Node(3)
root.right.right.right.right = Node(4)
root.right.right.right.right.right = Node(5)
