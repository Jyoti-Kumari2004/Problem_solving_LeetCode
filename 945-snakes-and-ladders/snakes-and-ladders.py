class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        q=deque()
        q.append([1,0])
        board.reverse()
        visited=set()
        while q:
            node,st=q.popleft()
            for i in range(1,7):
                x,y=self.solve(node+i,n)
                next=node+i
                if board[x][y]!=-1:
                    next=board[x][y]
                if next==n*n:
                    return st+1
                if next not in visited:
                    q.append([next,st+1])
                    visited.add(next)
        return -1
    def solve(self,num,n):
        r=(num-1)//n
        c=(num-1)%n
        if r%2:
            c=n-1-c
        return [r,c]


    





