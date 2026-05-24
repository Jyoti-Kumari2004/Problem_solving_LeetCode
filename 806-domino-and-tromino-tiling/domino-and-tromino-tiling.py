class Solution:
    def __init__(self):
        self.t=[-1]*1001
    def numTilings(self, n: int) -> int:
        return self.solve(n)
        
    def solve(self,n):
        if n==0:
            return 1
        if n==1:
            return 1
        elif n==2:
            return 2
        elif n==3:
            return 5
        elif self.t[n]!=-1:
            return self.t[n]
        else:
            self.t[n]=self.solve(n-1)*2 +self.solve(n-3)
            return self.t[n]%(10**9+7)


        