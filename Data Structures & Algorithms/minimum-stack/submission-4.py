class MinStack:
    stack=[]
    decreasing_stack=[]

    def __init__(self):
        print(self.decreasing_stack)
        self.decreasing_stack=[]
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.decreasing_stack:
            self.decreasing_stack.append(min(self.decreasing_stack[-1], val))
        else:
            self.decreasing_stack.append(val)
        print(self.decreasing_stack)

    def pop(self) -> None:
        self.stack.pop()
        self.decreasing_stack.pop()
        print(self.decreasing_stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.decreasing_stack[-1]
        
