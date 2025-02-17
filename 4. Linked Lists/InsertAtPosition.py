from linkedlist import LinkedList, Node, printList

def insertAtPosition(head: Node, position, x):
    if position == 0:
        newNode = Node(x)
        newNode.next = head
        head = newNode
        return head        

    i = 0
    t = head
    
    while i < position:
        if t is None:
            return head
        
        t = t.next
        i += 1
    
    newNode = Node(x)
    newNode.next = t.next
    t.next = newNode
    return head

list = LinkedList([1, 2, 3, 4, 5])
list = insertAtPosition(list.head, 0, 99)
printList(list)