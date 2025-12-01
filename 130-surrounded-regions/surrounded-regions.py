class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        visited_mat=[[0 for i in range(m)]for i in range(n)]
        for i in range(m):
            if board[0][i]=="O" and visited_mat[0][i]==0:
                self.dfs(0,i,board,visited_mat)
        for i in range(n):
            if board[i][0]=="O" and visited_mat[i][0]==0:
                self.dfs(i,0,board,visited_mat)
        for i in range(m):
            if board[n-1][i]=="O" and visited_mat[n-1][i]==0:
                self.dfs(n-1,i,board,visited_mat)
        for i in range(n):
            if board[i][m-1]=="O" and visited_mat[i][m-1]==0:
                self.dfs(i,m-1,board,visited_mat)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and visited_mat[i][j] == 0:
                    board[i][j] = "X"


        
    def dfs(self,x,y,board,visited_mat):
        dir=[[0,-1],[0,1],[1,0],[-1,0]]
        visited_mat[x][y]=1
        for i,j in dir:
            if 0<=x+i<len(board) and 0<=y+j<len(board[0]) and board[x+i][y+j]=="O" and visited_mat[x+i][y+j]==0:
                self.dfs(x+i,y+j,board,visited_mat)

        