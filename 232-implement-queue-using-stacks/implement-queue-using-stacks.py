class MyQueue:

    def __init__(self):
        self.stack=[]
        self.stack1=[]
    
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> int:
        while self.stack:
            self.stack1.append(self.stack.pop())
        ele=self.stack1.pop()
        while self.stack1:
            self.stack.append(self.stack1.pop())
        return ele
        

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        if not self.stack:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()