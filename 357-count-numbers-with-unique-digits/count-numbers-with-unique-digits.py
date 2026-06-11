class Solution:
    # this is very efficient solution using digitdp, only O(n) time and O(1) space
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        t=[0]*(n+1)
        t[0]=1
        k=10
        for i in range(n):
            if i==0:
                mul=9
            else:
                mul*=k
            k-=1
            t[i+1]=mul+t[i]
        return t[-1]

            

        


        # this is very naive approch using backtracking, took more time N^10 , and N space
    # def __init__(self):
    #     self.c=0
    # def countNumbersWithUniqueDigits(self, n: int) -> int:
    #     self.c=0
    #     s=set()
    #     self.solve(0,s,n)
    #     return self.c+1
    # def solve(self,ind,s,n):
    #     if ind==n:
    #         return 
    #     for i in range(10):
    #         if i==0 and ind==0:
    #             continue
    #         if i not in s:
    #             self.c+=1
    #             s.add(i)
    #             self.solve(ind+1,s,n)
    #             s.remove(i)