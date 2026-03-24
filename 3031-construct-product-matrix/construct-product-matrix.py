class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        #now i will apply prefix and suffix wala method
        res=[]
        for lis in grid:
            res.extend(lis)
        i=1
        prefpro=[0]*len(res)
        prefpro[0]=res[0]
        while i<len(res):
            prefpro[i]=(prefpro[i-1]*res[i])%12345
            i+=1
        j=len(res)-2
        sufpro=[0]*len(res)
        sufpro[-1]=res[-1]
        while j>=0:
            sufpro[j]=(sufpro[j+1]*res[j])%12345
            j-=1
        ans=[0]*len(res)
        ans[0]=sufpro[1]%12345
        ans[-1]=prefpro[-2]%12345
        for i in range(1,len(res)-1):
            ans[i]=(prefpro[i-1]*sufpro[i+1])%12345
        k=0
        fans=[]
        for i in range(len(grid)):
            l=[]
            for j in range(len(grid[i])):
                l.append(ans[k])
                k+=1
            fans.append(l)
        return fans
        