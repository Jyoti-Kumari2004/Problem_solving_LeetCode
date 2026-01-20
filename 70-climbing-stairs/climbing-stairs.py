class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solve(n)


    def solve(self,n):
        if n==1:
            return 1
        t=[None]*(n+1)
        t[0]=1
        t[1]=1
        for i in range(2,n+1):
            print(t)
            t[i]=t[i-1]+t[i-2]   
        return t[n-1]+t[n-2]
            