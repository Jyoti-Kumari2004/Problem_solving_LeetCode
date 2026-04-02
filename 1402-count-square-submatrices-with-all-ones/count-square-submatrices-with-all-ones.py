class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        t=[[0]*len(matrix[0]) for i in range(len(matrix))]
        for i in range(len(matrix)):
            if matrix[i][0]==1:
                t[i][0]=1
        for j in range(len(matrix[0])):
            if matrix[0][j]==1:
                t[0][j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    t[i][j]=1+min(t[i-1][j-1],t[i-1][j],t[i][j-1])
                else:
                    t[i][j]=0
        print(t)
        s=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s+=t[i][j]
        return s


        