class Solution:
    def __init__(self):
        self.t=[]
    def minCut(self, s: str) -> int:
        #recursive solution
            # return (self.solve(s,0,len(s)-1))

        #recursive+memoization(bottom_up dp)
            # return (self.bottom_up(s,0,len(s)-1))

        #more optimized bottom_up
        n=len(s)
        m=len(s)
        pt=[[False]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==j:
                    pt[i][j]=True
        for i in range(n-1,-1,-1):
            for j in range(m):
                if j>i:
                    l=j-i+1
                    if l==2 and s[i]==s[j]:
                        pt[i][j]=True
                    elif l==3 and s[i]==s[j]:
                        pt[i][j]=True
                    else:
                        if s[i]==s[j] and pt[i+1][j-1]:
                            pt[i][j]=True
                        else:
                            pt[i][j]=False
        n = len(s)
        self.t = [[-1]*n for _ in range(n)]
        return self.optimized_bottom_up(s,0,len(s)-1,pt)

    def optimized_bottom_up(self,s,i,j,pt):
        if i>=j or pt[i][j]:
            return 0
        if self.t[i][j]!=-1:
            return self.t[i][j]
        ans=float('inf')
        for k in range(i,j):
            if pt[i][k]:
                temp_ans=1+self.optimized_bottom_up(s,k+1,j,pt)
                ans=min(ans,temp_ans)
        self.t[i][j]=ans
        return self.t[i][j]

    # def bottom_up(self,s,i,j):
    #     if i>=j or self.isPanil(s[i:j+1]):
    #         return 0
    #     if self.t[i][j]!=-1:
    #         return self.t[i][j]
    #     ans=float('inf')
    #     for k in range(i,j):
    #         temp_ans=self.bottom_up(s,i,k)+self.bottom_up(s,k+1,j)+1
    #         ans=min(ans,temp_ans)
    #     self.t[i][j]=ans
    #     return self.t[i][j]


#recursive solution , take more time
    # def solve(self,s,i,j):
    #     if i>=j or self.isPanil(s[i:j+1]):
    #         return 0
    #     ans=float('inf')
    #     for k in range(i,j-1):
    #         temp_ans=self.solve(s,i,k)+self.solve(s,k+1,j)+1
    #         ans=min(ans,temp_ans)
    #     return ans

    # def isPanil(self,s):
    #     n=len(s)
    #     m=len(s)
    #     t=[[False]*m for i in range(n)]
    #     for i in range(n):
    #         for j in range(m):
    #             if i==j:
    #                 t[i][j]=True
    #     for i in range(n-1,-1,-1):
    #         for j in range(m):
    #             if j>i:
    #                 l=j-i+1
    #                 if l==2 and s[i]==s[j]:
    #                     t[i][j]=True
    #                 elif l==3 and s[i]==s[j]:
    #                     t[i][j]=True
    #                 else:
    #                     if s[i]==s[j] and t[i+1][j-1]:
    #                         t[i][j]=True
    #                     else:
    #                         t[i][j]=False

        
        