class Solution:
    def __init__(self):
        self.t=[[[-1]*71 for i in range(71)] for j in range(71)]
    def cherryPickup(self, grid: List[List[int]]) -> int:
        return self.solve(0,0,len(grid[0])-1,grid)


    def solve(self,i,j1,j2,grid):
        if i<0 or i>=len(grid) or j1<0 or j1>=len(grid[0]) or j2<0 or j2>=len(grid[0]):
            return float("-inf")
        if i==len(grid)-1:
            if j1==j2:
                return grid[i][j1]
            else:
                return grid[i][j1]+grid[i][j2]
        # if self.t[i][j][k]!=-1:
        #     return self.t[i][j][k]
        if self.t[i][j1][j2]!=-1:
            return self.t[i][j1][j2]
        
        ans=float("-inf")
        for dj1 in range(-1,2):
            for dj2 in range(-1,2):
                if j1==j2:
                    ch=grid[i][j1]+self.solve(i+1,j1+dj1,j2+dj2,grid)
                else:
                    ch=grid[i][j1]+grid[i][j2]+self.solve(i+1,j1+dj1,j2+dj2,grid) 
                ans=max(ans,ch)
        self.t[i][j1][j2]=ans
        return ans
        # if i1==i2 and j1==j2:
        #     ch1=grid[i1][j1]+self.solve(i1+1,j1-1,i2+1,j2-1,grid)
        #     ch4=grid[i1][j1]+self.solve(i1+1,j1-1,i2+1,j2+1,grid)
        #     ch5=grid[i1][j1]+self.solve(i1+1,j1-1,i2+1,j2,grid)

        #     ch2=grid[i1][j1]+self.solve(i1+1,j1,i2+1,j2-1,grid)
        #     ch6=grid[i1][j1]+self.solve(i1+1,j1,i2+1,j2+1,grid)
        #     ch7=grid[i1][j1]+self.solve(i1+1,j1,i2+1,j2,grid)

        #     ch3=grid[i1][j1]+self.solve(i1+1,j1+1,i2+1,j2-1,grid)
        #     ch8=grid[i1][j1]+self.solve(i1+1,j1+1,i2+1,j2+1,grid)
        #     ch9=grid[i1][j1]+self.solve(i1+1,j1+1,i2+1,j2,grid)
        #     return max(ch1,ch2,ch3,ch4,ch5,ch6,ch7,ch8,ch9)
        # else:
        #     ch1=grid[i1][j1]+grid[i2][j2]+self.solve(i1+1,j1-1,i2+1,j2-1,grid)
        #     ch4=grid[i1][j1]+grid[i2][j2]+self.solve(i1+1,j1-1,i2+1,j2+1,grid)
        #     ch5=grid[i1][j1]+grid[i2][j2]+self.solve(i1+1,j1-1,i2+1,j2,grid)

        #     ch2=grid[i1][j1]+grid[i2][j2]+self.solve(i1+1,j1,i2+1,j2-1,grid)
        #     ch6=grid[i1][j1]+grid[i2][j2]+self.solve(i1+1,j1,i2+1,j2+1,grid)
        #     ch7=grid[i1][j1]+grid[i2][j2]+self.solve(i1+1,j1,i2+1,j2,grid)

        #     ch3=grid[i1][j1]+grid[i2][j2]+self.solve(i1+1,j1+1,i2+1,j2-1,grid)
        #     ch8=grid[i1][j1]+grid[i2][j2]+self.solve(i1+1,j1+1,i2+1,j2+1,grid)
        #     ch9=grid[i1][j1]+grid[i2][j2]+self.solve(i1+1,j1+1,i2+1,j2,grid)

            
        
        