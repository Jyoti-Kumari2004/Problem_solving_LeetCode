class Solution:
    def __init__(self):
        self.t=[[-1]*201 for i in range(201)]
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        # return self.solve(0,0,n,triangle)
        t=[[float('inf')]*len(triangle[n-1]) for i in range(n)]
        curr_sum=0
        for i in range(n):
            curr_sum+=triangle[i][0]
            t[i][0]=curr_sum

        for i in range(1,n):
            for j in range(1,len(triangle[i])):
                t[i][j]=triangle[i][j]+min(t[i-1][j],t[i-1][j-1])
        return min(t[n-1])







    #memoization solution
    # def solve(self,i,j,n,triangle):
    #     if i>=n-1:
    #         return triangle[n-1][j]
    #     if self.t[i][j]!=-1:
    #         return self.t[i][j]
    #     d=triangle[i][j]+self.solve(i+1,j,n,triangle)
    #     dig=triangle[i][j]+self.solve(i+1,j+1,n,triangle)
    #     self.t[i][j]=min(d,dig)
    #     return min(d,dig)
    
    #recurrsive solution
    # def solve(self,i,j,n,triangle):
    #     if i>=n-1:
    #         return triangle[n-1][j]
    #     d=triangle[i][j]+self.solve(i+1,j,n,triangle)
    #     dig=triangle[i][j]+self.solve(i+1,j+1,n,triangle)
    #     return min(d,dig)

        