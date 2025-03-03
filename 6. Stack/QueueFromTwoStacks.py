class Queue:
    # Doesn't work on geeks for geeks but I don't know why. Other official solutions didn't work either...
    s1 = []
    s2 = []
    
    def enqueue(self,X):
        self.s1.append(X)
            
    def dequeue(self):
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
            
        popped = self.s2.pop()
        
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
            
        return popped