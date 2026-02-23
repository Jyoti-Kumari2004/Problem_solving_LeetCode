class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for i in range(n)]
        res=[]
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
            if self.isValid(n,i,col,board):
                board[i][col]="Q"
                self.solve(n,res,col+1,board)
                board[i][col]="."
    def isValid(self,n,row,col,board):
        ori_row=row
        ori_col=col
        
        while 0<=row<n and 0<=col<n:
            if board[row][col]=="Q":
                return False
            row-=1
            col-=1
        row=ori_row
        col=ori_col
        while 0<=row<n and 0<=col<n:
            if board[row][col]=="Q":
                return False
            col-=1
        row=ori_row
        col=ori_col
        while 0<=row<n and 0<=col<n:
            if board[row][col]=="Q":
                return False
            col-=1
            row+=1
        return True



    
    # def solve(self,n,path,res,row,col,board,visited):
    #     if col==n:
    #         res.append(path.copy())
    #         return 
    #     for i in range(0,n):
    #         if visited[col][i]==False:

    #             for k in range(0,n):
    #                 visited[row][k]=True
    #                 visited[k][col]=True
    #                 if 0 <= row+i < n and 0 <= col+i < n:
    #                     visited[row+i][col+i] = True
    #                 if 0 <= row-i < n and 0 <= col-i < n:
    #                     visited[row-i][col-i] = True
    #                 if 0 <= row+i < n and 0 <= col-i < n:
    #                     visited[row+i][col-i] = True
    #                 if 0 <= row-i < n and 0 <= col+i < n:
    #                     visited[row-i][col+i] = True
    #             st="."*i
    #             st+="Q"
    #             st+="."*(n-i-1)
    #             path.append(st)
    #             self.solve(n,path,res,i,col+1,board,visited)
    #             path.pop()
    #             for k in range(0,n):
    #                 visited[row][k]=False
    #                 visited[k][col]=False
    #                 if 0 <= row+i < n and 0 <= col+i < n:
    #                     visited[row+i][col+i] = False
    #                 if 0 <= row-i < n and 0 <= col-i < n:
    #                     visited[row-i][col-i] = False
    #                 if 0 <= row+i < n and 0 <= col-i < n:
    #                     visited[row+i][col-i] = False
    #                 if 0 <= row-i < n and 0 <= col+i < n:
    #                     visited[row-i][col+i] = False
            

    
