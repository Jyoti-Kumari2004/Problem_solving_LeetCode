class Solution:
    def __init__(self):
        self.row_side=[]
        self.up_dg=[]
        self.down_dg=[]
    def totalNQueens(self, n: int) -> int:
        board=[["."]*n for i in range(n)]
        res=[0]
        self.row_side=[False]*n
        self.up_dg=[False]*((2*n)-1)
        self.down_dg=[False]*((2*n)-1)
        self.solve(n,res,0,board)
        return res[0]

    def solve(self,n,res,col,board):
        if col==n:
            res[0]+=1
            return 
        for i in range(0,n):
            if self.row_side[i]==False and self.up_dg[(n-1)+(col-i)]==False and self.down_dg[i+col]==False:
                self.row_side[i]=True
                self.up_dg[(n-1)+(col-i)]=True
                self.down_dg[i+col]=True

                self.solve(n,res,col+1,board)

                board[i][col]="."

                self.row_side[i]=False
                self.up_dg[(n-1)+(col-i)]=False
                self.down_dg[i+col]=False
        