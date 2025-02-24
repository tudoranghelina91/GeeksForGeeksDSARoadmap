from linkedlist import Node, LinkedList;

def countNodesInCircular(head: Node):
    t = head
    cnt = 0
    while True:
        cnt += 1
        if t.next is not None:
            t = t.next
        if t == head:
            break

    return cnt

circularList = LinkedList([1], True)

print(countNodesInCircular(circularList.head))