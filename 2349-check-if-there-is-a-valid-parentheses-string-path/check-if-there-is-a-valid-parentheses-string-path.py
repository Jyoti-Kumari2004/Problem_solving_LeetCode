class Solution:
    def __init__(self):
        self.t={}
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        if grid[0][0]==")" or grid[n-1][m-1]=="(":
            return False
        if (m+n-1)%2!=0:
            return False
        return self.solve(0,0,0,grid)
            
        
    def solve(self,i,j,op,grid):
        if op<0:
            return False
        if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0:
            return False
        if i==len(grid)-1 and j==len(grid[0])-1:
            if grid[i][j]==")":
                op-=1
            else:
                op+=1
            return op==0
        if (i,j,op) in self.t:
            return self.t[(i,j,op)]
            
        if grid[i][j]=="(":
            ch=self.solve(i+1,j,op+1,grid)
            ch2=self.solve(i,j+1,op+1,grid)
            ans=ch or ch2
        else:
            ch=self.solve(i+1,j,op-1,grid)
            ch2=self.solve(i,j+1,op-1,grid)
            ans=ch or ch2
        self.t[(i,j,op)]=ans
        return ans
