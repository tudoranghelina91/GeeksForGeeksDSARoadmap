from linkedlist import LinkedList, Node


def printList(head: Node):
    print(head.data, end =" ")
    t = head.next
    while t is not head:
        print(t.data, end= " ")
        t = t.next

list = LinkedList([1, 2, 3, 4, 5], True)
printList(list.head)