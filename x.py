class MyQueue:

    # def __init__(self):
    #     self.stack = []
    #     self.temp = []

    # def push(self, x: int) -> None:
    #     self.stack.append(x)
        
    # def pop(self) -> int:
    #     while self.stack:
    #         self.temp.append(self.stack.pop())
    #     if self.temp:
    #         val = self.temp.pop()
    #     while self.temp:
    #         self.stack.append(self.temp.pop())
    #     return val

    # def peek(self) -> int:
    #     return self.stack[0]
        
    # def empty(self) -> bool:
    #     return len(self.stack) == 0
    
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        
    def _shift(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        
    def pop(self) -> int:
        self._shift()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._shift()
        return self.out_stack[-1]
        
    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()