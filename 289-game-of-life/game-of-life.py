class Solution(object):
    def __init__(self):
        self.dir = [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                count=0
                for x,y in self.dir:
                    nx=x+i
                    ny=y+j
                    if 0<=nx<n and 0<=ny<m and (board[nx][ny]==1 or board[nx][ny]==-1):
                        count+=1
                if board[i][j]==1:
                    if count<2 or count>3:
                        board[i][j]=-1
                elif count==3 and board[i][j]==0:
                    board[i][j]=2
        for i in range(n):
            for j in range(m):
                if  board[i][j]==2:
                    board[i][j]=1
                elif board[i][j]==-1:
                    board[i][j]=0

            
                
        