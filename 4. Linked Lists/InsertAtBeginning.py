from linkedlist import Node, LinkedList, printList

def insertAtBegining(head, x):
    aux = head
    head = Node(x)
    head.next = aux
    return head

list = LinkedList([1, 2, 3, 4, 5])
newHead = insertAtBegining(list.head, 6)
printList(newHead)