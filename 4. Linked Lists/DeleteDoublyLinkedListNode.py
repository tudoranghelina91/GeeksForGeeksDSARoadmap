def delete_node(head, x):
    #code here
    
    if x == 1:
        head.next.prev = None
        head = head.next
        # return head
        
    else:
        cnt = 1
        t = head
        while cnt < x - 1:
            t = t.next
            cnt += 1
        
        if t.next is not None and t.next.next is not None:
            t.next = t.next.next
            t.next.prev = t
        
        else:
            t.next.prev = None
            t.next = None
    
    return head