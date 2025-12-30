class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if len(grid)<3 or len(grid[0])<3:
            return 0
        count=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                mat = [row[j:j+3] for row in grid[i:i+3]]
                if self.checkmat(mat):
                    count+=1
        return count
    def checkmat(self,mat):
        d=defaultdict(int)
        for i in range(3):
            for j in range(3):
                if mat[i][j]<1 or mat[i][j]>9 or d[mat[i][j]]==1:
                    return False
                d[mat[i][j]]+=1

        x=mat[0][0]+mat[1][1]+mat[2][2]
        y=mat[0][2]+mat[1][1]+mat[2][0]

        a=mat[0][0]+mat[0][1]+mat[0][2] #r1
        b=mat[1][0]+mat[1][1]+mat[1][2] #r2
        c=mat[2][0]+mat[2][1]+mat[2][2] #r3

        i=mat[0][0]+mat[1][0]+mat[2][0] #c1
        j=mat[0][1]+mat[1][1]+mat[2][1] #c2
        k=mat[0][2]+mat[1][2]+mat[2][2] #c3
        if x==y==a==b==c==i==j==k:
            return True
        else:
            return False
                

        