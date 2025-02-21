class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data: list, circular: bool = False):
        self.head = Node(data[0])
        t = self.head
        for i in range(1, len(data)):
            t.next = Node(data[i])
            
            if i == len(data) - 1 and circular:
                t.next.next = self.head
            
            t = t.next

def printList(head):
    t = head
    while (t != None):
        print(t.data, end= " ")
        t = t.next
        if t == head:
            break
    print()