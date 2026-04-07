class MinStack:

    def __init__(self):
        self.mini_ele=0
        self.st=[]
        

    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.st.append(val)
            self.mini_ele=val
        else:
            if val>self.mini_ele:
                self.st.append(val)
            else:
                self.st.append(2*val-self.mini_ele)
                self.mini_ele=val

    def pop(self) -> None:
        if self.mini_ele<self.st[-1]:
            self.st.pop()
        else:
            self.mini_ele=2*self.mini_ele-self.st[-1]
            self.st.pop()


        

    def top(self) -> int:
        if self.st[-1]<self.mini_ele:
            return self.mini_ele
        return self.st[-1]
        

    def getMin(self) -> int:
        if not self.st:
            return -1
        else:
            return self.mini_ele
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#this solution takes O(n) space, we need to optimize thissssssssss,
    # def __init__(self):
    #         self.ans_st=[]
    #         self.st=[]
            

    #     def push(self, val: int) -> None:
    #         self.st.append(val)
    #         if not self.ans_st or val<=self.ans_st[-1]:
    #             self.ans_st.append(val)


    #     def pop(self) -> None:
    #         x=self.st.pop()
    #         if x==self.ans_st[-1]:
    #             self.ans_st.pop()
            

    #     def top(self) -> int:
    #         return self.st[-1]
            