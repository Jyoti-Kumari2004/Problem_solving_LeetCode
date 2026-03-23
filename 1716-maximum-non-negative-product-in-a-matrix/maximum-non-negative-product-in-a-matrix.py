class Solution:
    def __init__(self):
        self.t=[[None]*16 for i in range(16)]
    def maxProductPath(self, grid: List[List[int]]) -> int:
        x=self.solve(len(grid)-1,len(grid[0])-1,grid)
        print(x)
        if x[0]<0:
            return -1
        return x[0]%1000000007

    def solve(self,i,j,grid):
        if i==0 and j==0:
            return [grid[0][0],grid[0][0]]
        if self.t[i][j]!=None:
            return self.t[i][j]
        vals=[]
        if j>0:
            maxl,minl=self.solve(i,j-1,grid)
            maxl=maxl*grid[i][j]
            minl=minl*grid[i][j]
            vals+=[maxl,minl]
        if i>0:
            maxu,minu=self.solve(i-1,j,grid)
            maxu=maxu*grid[i][j]
            minu=minu*grid[i][j]
            vals+=[maxu,minu]
        nmax=max(vals)
        nmin=min(vals)
        self.t[i][j]=[nmax,nmin]
        return self.t[i][j]
        


        