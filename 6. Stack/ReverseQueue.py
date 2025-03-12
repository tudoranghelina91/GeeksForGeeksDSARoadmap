from queue import Queue

def reverseQueue(q):
    # code here
    st = []
    while not q.empty():
        st.append(q.get())
    
    while st:
        q.put(st.pop())
        
    return q

if __name__ == "__main__":

    q = Queue()
    for i in range(1, 6):
        q.put(i)
    
    reverseQueue(q)
    while not q.empty():
        print(q.get(), end=" ")