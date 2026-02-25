class Solution:
    def __init__(self):
        self.dir=[[-1,0],[0,1],[1,0],[0,-1]]

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=[[False]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0]==board[i][j]:
                    visited[i][j]=True
                    if self.solve(0,board,i,j,word,[word[0]],visited):
                        return True
                    visited[i][j]=False

        return False
    
    def solve(self,curr_ind,board,i,j,word,path,visited):
        if curr_ind==len(word)-1:
            return True
        if len(path)>len(word):
            return False
        for x,y in self.dir:
            nx=i+x
            ny=j+y
            if 0<=nx<len(board) and 0<=ny<len(board[0]) and visited[nx][ny]==False and board[nx][ny]==word[curr_ind+1]:
                path.append(board[nx][ny])
                visited[nx][ny]=True
                if self.solve(curr_ind+1,board,nx,ny,word,path,visited):
                    return True
                path.pop()
                visited[nx][ny]=False
        
        