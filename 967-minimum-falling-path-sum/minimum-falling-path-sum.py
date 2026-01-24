class Solution:
    # def __init__(self):
    #     self.t=[[-1]*101 for i in range]
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # ans=float('inf')
        # for i in range(len(matrix[0])):
        #     ans=min(ans,self.solve(0,i,len(matrix),matrix))
        # return ans

        #top-down approach
        n=len(matrix)
        t=[[float('inf')]*n for i in range(n)]
        for i in range(len(matrix[0])):
            t[0][i]=matrix[0][i]
        
        for i in range(1,n):
            for j in range(n):
                if j==0:
                    t[i][j]=matrix[i][j]+min(t[i-1][j],t[i-1][j+1])
                elif j==n-1:
                    t[i][j]=matrix[i][j]+min(t[i-1][j-1],t[i-1][j])
                else:
                    t[i][j]=matrix[i][j]+min(t[i-1][j-1],t[i-1][j],t[i-1][j+1])


        return min(t[n-1])



    #memoization solution
    def solve(self,i,j,n,matrix):
        if i<0 or j<0 or i>n-1 or j>n-1:
            return float('inf')
        if i==n-1:
            return matrix[i][j]
        if self.t[i][j]!=-1:
            return self.t[i][j]
        dg1=matrix[i][j]+self.solve(i+1,j-1,n,matrix)
        dg2=matrix[i][j]+self.solve(i+1,j+1,n,matrix)
        down=matrix[i][j]+self.solve(i+1,j,n,matrix)
        self.t[i][j]=min(dg1,dg2,down)
        return min(dg1,dg2,down)

    #recurrsive solution

    # def solve(self,i,j,n,matrix):
    #     if i<0 or j<0 or i>n-1 or j>n-1:
    #         return float('inf')
    #     if i==n-1:
    #         return matrix[i][j]
    #     dg1=matrix[i][j]+self.solve(i+1,j-1,n,matrix)
    #     dg2=matrix[i][j]+self.solve(i+1,j+1,n,matrix)
    #     down=matrix[i][j]+self.solve(i+1,j,n,matrix)
    #     return min(dg1,dg2,down)
        