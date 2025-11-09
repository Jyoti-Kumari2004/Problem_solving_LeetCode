
class Solution:
    def floodFill(self, grid: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n,m=len(grid),len(grid[0])
        q=deque()
        gcolor=grid[sr][sc]
        if gcolor==color:
            return grid
        q.append((sr,sc))
        grid[sr][sc]=color
        dir=[[-1,0],[1,0],[0,-1],[0,1]]
        while q:
            i,j=q.popleft()
            for x,y in dir:
                nr=i+x
                nc=j+y
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==gcolor:
                    grid[nr][nc]=color
                    q.append((nr,nc))
        return grid

        
        