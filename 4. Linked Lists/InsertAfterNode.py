from linkedlist import LinkedList, Node, printList

def insertAfterNode(head, key, x):
    t = head

    while t is not None and t.data != key:
        t = t.next

    if t is None:
        return head

    newNode = Node(x)
    newNode.next = t.next
    t.next = newNode

    return head

list = LinkedList([1,2,3,4])
newlist = insertAfterNode(list.head, 3, 5)
printList(newlist)