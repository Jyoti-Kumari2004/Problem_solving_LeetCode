class Solution:
    def __init__(self):
        self.roww=[]
        self.coll=[]
        self.boxes=[]

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        """   
        self.roww=[[False]*10 for i in range(9)]
        self.coll=[[False]*10 for i in range(9)]
        self.boxes=[[False]*10 for i in range(9)]     
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    num = int(board[r][c])
                    box = (r//3)*3 + (c//3)
                    self.roww[r][num] = True
                    self.coll[c][num] = True
                    self.boxes[box][num] = True
        self.solve(board)
            

    def solve(self,board):
        
        for j in range(0,9):
            for k in range(0,9):
                if board[j][k]==".":
                    box = (j//3)*3 + (k//3)
                    for c in range(1,10):
                        if self.roww[j][c]==False and self.coll[k][c]==False and self.boxes[box][c]==False:
                            board[j][k]=str(c)
                            self.roww[j][c]=True
                            self.coll[k][c]=True
                            self.boxes[box][c]=True
                            if self.solve(board):
                                return True
                            board[j][k]="."
                            self.roww[j][c]=False
                            self.coll[k][c]=False
                            self.boxes[box][c]=False
                                
                    return False
        return True
                    
    # def isValid(self,board,row,col,k):
    #     for i in range(0,9):
    #         if board[row][i]==k: 
    #             return False
    #         if board[i][col]==k:
    #             return False
    #         if  board[3*(row//3)+i//3][3*(col//3)+i%3]==k:
    #             return False
    #     return True




