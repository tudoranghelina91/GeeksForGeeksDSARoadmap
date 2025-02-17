from linkedlist import LinkedList, Node

def count(head: Node, key):
    t = head
    cnt = 0
    while t is not None:
        if t.data == key:
            cnt += 1
        
        t = t.next
    
    return cnt

list = LinkedList([1, 2, 1, 2, 1, 3, 1])
print(count(list.head, 1))