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
            t = t.next

        if circular:
            t.next = self.head

def printList(head):
    t = head
    while (t != None):
        print(t.data, end= " ")
        t = t.next
        if t == head:
            print("-> " + str(t.data), end=" ")
            break
    print()