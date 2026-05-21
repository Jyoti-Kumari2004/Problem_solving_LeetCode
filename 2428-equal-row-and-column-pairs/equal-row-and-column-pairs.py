class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        gridd=[[0]*len(grid[0]) for i in range(len(grid))]
        count=0
        for i in range(len(grid)):
            k=len(grid[0])
            val=0
            for j in range(len(grid[0])):
                val+=grid[i][j]*(37**k)
                k-=1
            for j in range(len(grid[0])):
                gridd[i][j]=val
        for i in range(len(grid[0])):
            k=len(grid)
            val=0
            for j in range(len(grid)):
                val+=grid[j][i]*(37**k)
                k-=1
            for j in range(len(grid[0])):
                if val==gridd[j][i]:
                    count+=1
        
        return count




        