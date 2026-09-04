class MinStack:

    def __init__(self):
        self.stack = [] # values
        self.minStack = [] # min values by index of self.stack
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.minStack:
            self.minStack.append(min(self.minStack[-1], val))
        else:
            self.minStack.append(val)
        
    def pop(self) -> None:
        if not self.stack:
            return None

        last_val = self.stack[-1] 
        self.stack = self.stack[:-1] # remove last element
        self.minStack = self.minStack[:-1]
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]

        
