class Solution:
    def __init__(self):
        self.dir=[[0,1],[1,0],[-1,0],[0,-1]]
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans=[[0]*len(mat[0]) for i in range(len(mat))]
        vis=set()
        q=deque()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    q.append((i,j,0))
                    vis.add((i,j))
        
        while q:
            ci,cj,st=q.popleft()
            for x,y in self.dir:
                nx=x+ci
                ny=y+cj
                if 0<=nx<len(mat) and 0<=ny<len(mat[0]) and (nx,ny) not in vis:
                    if mat[nx][ny]==1:
                        ans[nx][ny]=st+1
                        q.append((nx,ny,st+1))
                        vis.add((nx,ny))
        return ans
                    
                    
    # def bfs(self,i,j,mat):
    #     q=deque()
    #     q.append([i,j,0])
    #     vis=set()
    #     vis.add((i,j))
    #     while q:
    #         ci,cj,st=q.popleft()
    #         for x,y in self.dir:
    #             nx=x+ci
    #             ny=y+cj
    #             if 0<=nx<len(mat) and 0<=ny<len(mat[0]) and (nx,ny) not in vis:
    #                 if mat[nx][ny]==0:
    #                     return st+1
    #                 else:
    #                     q.append([nx,ny,st+1])
    #                     vis.add((nx,ny))
    #     return -1