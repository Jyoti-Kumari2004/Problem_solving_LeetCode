class Solution:
    def __init__(self):
        self.t=[-1]*1001

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        x=self.solve(len(cost)-1,cost)
        y=self.solve(len(cost)-2,cost)
        return min(x,y)

    def solve(self,i,cost):
        if i==1 or i==0:
            return cost[i]
        if self.t[i]!=-1:
            return self.t[i]
        ch1=cost[i]+self.solve(i-1,cost)
        ch2=cost[i]+self.solve(i-2,cost)
        self.t[i]=min(ch1,ch2)
        return self.t[i]
        