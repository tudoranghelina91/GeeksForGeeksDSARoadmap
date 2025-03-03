# For some reason test case doesn't pass when submitting solution but passes individually

class TwoStacks:
    def __init__(self):
        return
    
    twoStacks = []
    s1end = 0
    
    # Function to push an integer into stack 1
    def push1(self, x):
        self.twoStacks.insert(self.s1end, x)
        self.s1end += 1

    # Function to push an integer into stack 2
    def push2(self, x):
        self.twoStacks.append(x)

    # Function to remove an element from top of stack 1
    def pop1(self):
        if len(self.twoStacks) == 0 or self.s1end < 0:
            return -1
        
        self.s1end -= 1
        return self.twoStacks.pop(self.s1end)

    # Function to remove an element from top of stack 2
    def pop2(self):
        if len(self.twoStacks) == 0:
            return -1
        
        return self.twoStacks.pop()