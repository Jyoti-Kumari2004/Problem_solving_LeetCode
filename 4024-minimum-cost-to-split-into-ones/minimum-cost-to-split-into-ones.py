class Solution:
    def __init__(self):
        self.cost=0
    def minCost(self, n: int) -> int:
        ans=0
        for i in range(n):
            ans+=i
        return ans
    # def solve(self,n):
    #     if n<0:
    #         return 
    #     if n==1:
    #         return 
    #     a=n//2
    #     b=n-a
    #     self.cost+=a*b
    #     self.solve(n//2)
    #     self.solve(n-a)
        
            
        