class MinStack:

    def __init__(self):
        self.ans_st=[]
        self.st=[]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.ans_st or val<=self.ans_st[-1]:
            self.ans_st.append(val)


    def pop(self) -> None:
        x=self.st.pop()
        if x==self.ans_st[-1]:
            self.ans_st.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.ans_st[-1] 
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()