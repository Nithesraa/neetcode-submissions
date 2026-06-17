class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ministack or val <= self.ministack[-1]:
            self.ministack.append(val)
        
        

    def pop(self) -> None:
        if self.stack:
            top = self.stack.pop()
            if top == self.ministack[-1]:
                self.ministack.pop()
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if self.ministack:
            return self.ministack[-1]

        
