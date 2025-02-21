from linkedlist import LinkedList

def printListRecursive(head):
    if (head is None):
        print() # just to add a space
        return
    
    print(head.data, end=" ")
    printListRecursive(head.next)

def printListIterative(head):
    while (head is not None):
        print(head.data, end=" ")
        head = head.next
    print()

printListRecursive(LinkedList([5, 8, 1, 2]).head)
printListIterative(LinkedList([5, 8, 1, 2]).head)