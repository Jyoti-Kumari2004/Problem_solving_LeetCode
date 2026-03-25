class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        hori=[0]*len(grid)
        curr=0
        s=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                s+=grid[i][j]
        curr=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr+=grid[i][j]
            if curr==s-curr:
                    return True 
        curr=0
        for j in range(len(grid[0])):
            for i in range(len(grid)):
                curr+=grid[i][j]
            if curr==s-curr:
                return True
        return False
        # hs=s
        # vs=s
        # for i in range(len(hori)):
        #     if hori[i]==hs-hori[i]:
        #         return True
        # for j in range(len(veri)):
        #     if veri[j]==vs-veri[j]:
        #         return True
        
        # return False

