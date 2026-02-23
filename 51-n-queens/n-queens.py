class Solution:
    def __init__(self):
        self.row_side=[]
        self.up_dg=[]
        self.down_dg=[]
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        res=[]
        self.row_side=[False]*n
        self.up_dg=[False]*((2*n)-1)
        self.down_dg=[False]*((2*n)-1)
        self.solve(n,res,0,board)
        return res
    def solve(self,n,res,col,board):
        if col==n:
            path=[]
            for lis in board:
                path.append("".join(lis))

            res.append(path.copy())
            return 
        for i in range(0,n):
            
            if self.row_side[i]==False and self.up_dg[(n-1)+(col-i)]==False and self.down_dg[i+col]==False: 
             
                board[i][col]="Q" 

                self.row_side[i]=True
                self.up_dg[(n-1)+(col-i)]=True
                self.down_dg[i+col]=True

                self.solve(n,res,col+1,board)

                board[i][col]="."

                self.row_side[i]=False
                self.up_dg[(n-1)+(col-i)]=False
                self.down_dg[i+col]=False
    # def isValid(self,n,row,col,board):
    #     ori_row=row
    #     ori_col=col
        
    #     while 0<=row<n and 0<=col<n:
    #         if board[row][col]=="Q":
    #             return False
    #         row-=1
    #         col-=1
    #     row=ori_row
    #     col=ori_col
    #     while 0<=row<n and 0<=col<n:
    #         if board[row][col]=="Q":
    #             return False
    #         col-=1
    #     row=ori_row
    #     col=ori_col
    #     while 0<=row<n and 0<=col<n:
    #         if board[row][col]=="Q":
    #             return False
    #         col-=1
    #         row+=1
    #     return True



    
