class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, data: list):
        if len(data) == 0:
            return None
        
        self.head = Node(data[0])
        t = self.head
        for i in range(1, len(data)):
            aux = t
            t.next = Node(data[i])
            t = t.next
            t.prev = aux

def printList(head):
    t = head
    while (t != None):
        if t.next is None:
            print(t.data, end="")
        else:
            print(t.data, end= "<->")
        t = t.next
    print()