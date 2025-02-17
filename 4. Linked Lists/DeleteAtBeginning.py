from linkedlist import LinkedList, Node, printList

def deleteAtBeginning(head: Node):
    temp = head
    head = head.next
    del temp # actual deletion (clear up used memory)
    # print(temp) # this throws an exception...
    return head

list = LinkedList([1, 5, 8, 99, 3])
list = deleteAtBeginning(list.head)
printList(list)