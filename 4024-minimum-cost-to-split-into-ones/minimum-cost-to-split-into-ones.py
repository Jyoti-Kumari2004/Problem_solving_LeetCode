class Solution:
    def __init__(self):
        self.cost=0
    def minCost(self, n: int) -> int:
        return n*(n-1)//2
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
        
            
        