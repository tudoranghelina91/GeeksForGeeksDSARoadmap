from linkedlist import LinkedList

def searchKeyRecursive(head, key):
    #Code here
    if head is None:
        return False
    elif head.data == key:
        return True
    else:
        return searchKeyRecursive(head.next, key)
    
def searchKeyIterative(head, key):
    #Code here
    while head is not None:
        if head.data == key:
            return True

        head = head.next
    
    return False
    
list = LinkedList([1, 5, 2, 3, 7])
print(searchKeyRecursive(list.head, 3))
print(searchKeyIterative(list.head, 3))