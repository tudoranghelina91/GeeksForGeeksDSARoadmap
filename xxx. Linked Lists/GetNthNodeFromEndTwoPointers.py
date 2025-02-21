from linkedlist import LinkedList, Node


def getNthNodeFromEndTwoPointers(head: Node, n):
    i = 0
    start = head
    end = head

    while i < n:
        end = end.next
        i += 1

    while end is not None:
        start = start.next
        end = end.next

    return start

list = LinkedList([1, 2, 3, 4, 5])
o = getNthNodeFromEndTwoPointers(list.head, 3)
print(o.data)