class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # return self.solve(len(obstacleGrid[0])-1,len(obstacleGrid)-1,obstacleGrid)
        if obstacleGrid[0][0]==1:
            return 0
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        
        t=[[None]*m for i in range(n)]
        for i in range(n):
            t[i][0]=1
            if obstacleGrid[i][0]==1:
                for a in range(i,n):
                    t[a][0]=0
                break
        for j in range(m):
            t[0][j]=1
            if obstacleGrid[0][j]==1:
                for a in range(j,m):
                    t[0][a]=0
                break
            
            
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1:
                    t[i][j]=0
                else:
                    t[i][j]=t[i-1][j]+t[i][j-1]
        print(t)
        return t[n-1][m-1]

#recussive solution
    # def solve(self,i,j,mat):
    #     if i==0 and j==0:
    #         return 1
    #     if i<0 or j<0:
    #         return 0
    #     if mat[i][j]==1:
    #         return 0
    #     r=self.solve(i,j-1,mat)
    #     d=self.solve(i-1,j,mat)
    #     return r+d
        