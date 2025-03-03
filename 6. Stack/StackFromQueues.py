#User function Template for python3
'''
    :param x: value to be inserted
    :return: None

    queue_1 = Queue() # first queue
    queue_2 = Queue() # second queue
   '''
from queue import Queue   
   
#Function to push an element into stack using two queues.
def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    queue_1.put(x)

#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    
    if queue_1.empty():
        return -1
    while queue_1.qsize() > 1:
        queue_2.put(queue_1.get())
        
    popped = queue_1.get()
    queue_1, queue_2 = queue_2, queue_1
    return popped