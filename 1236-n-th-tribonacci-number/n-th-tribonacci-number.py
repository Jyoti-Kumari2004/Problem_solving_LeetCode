class Solution:
    def tribonacci(self, n: int) -> int:
        # t=[0]*(n+1)
        # t[0]=0
        # t[1]=1
        # t[2]=1
        pv=0
        pv1=1
        pv2=1
        curr=0
        if n==0 or n==1:
            return n
        elif n==2:
            return 1
        for i in range(3,n+1):
            curr=pv+pv1+pv2
            pv=pv1
            pv1=pv2
            pv2=curr
        return curr
        # return self.solve(n)
    # def solve(self,n):
    #     if n==0 or n==1:
    #         return n
    #     if n==2:
    #         return 1
    #     return self.solve(n-1)+self.solve(n-3)+self.solve(n-2)
        