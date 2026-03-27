class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        res=[[0 for j in range(i)] for i in range(1,numRows+1)]
        for i in range(numRows):
            res[i][0]=1
        for i in range(numRows):
            res[i][-1]=1
        for i in range(2,numRows):
            for j in range(1,i):
                if res[i][j]==0:
                    res[i][j]=res[i-1][j-1]+res[i-1][j] 
        return res