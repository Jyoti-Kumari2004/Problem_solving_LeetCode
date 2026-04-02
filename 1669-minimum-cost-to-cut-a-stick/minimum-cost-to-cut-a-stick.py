class Solution:
    def __init__(self):
        self.t=[[None]*101 for i in range(101)]
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts=[0]+cuts+[n] 
        ans=self.solve(cuts,1,len(cuts)-2) 
        if ans==float('inf'):
            return -1
        return ans

    def solve(self,cuts,i,j):
        if i>j:
            return 0
        if self.t[i][j]!=None:
            return self.t[i][j]
        ans=float('inf')
        for k in range(i,j+1):
            temp_ans=cuts[j+1]-cuts[i-1]+ self.solve(cuts,i,k-1) + self.solve(cuts,k+1,j)
            ans=min(ans,temp_ans)
        self.t[i][j]=ans
        return ans