from linkedlist import LinkedList

def getCount(head):
    # code here
    cnt = 0
    while (head != None):
        head = head.next
        cnt += 1
    return cnt

list = LinkedList([12, 5, 8, 3, 2, 7])

print(getCount(list.head))