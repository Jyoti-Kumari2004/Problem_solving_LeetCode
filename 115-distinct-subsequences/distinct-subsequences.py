class Solution:
    def __init__(self):
        self.p=[[-1]*1001 for i in range(1001)]
    def numDistinct(self, s: str, t: str) -> int:
        return self.solve(s,t,len(s),len(t))
        

    def solve(self,s,t,i,j):
        if j==0:
            return 1
        if i==0:
            return 0
        if self.p[i][j]!=-1: 
            return self.p[i][j]
        if s[i-1]==t[j-1]:
            if self.p[i-1][j-1]!=-1:
                l=self.p[i-1][j-1]
            else:
                l=self.solve(s,t,i-1,j-1)
            if self.p[i-1][j]!=-1:
                r=self.p[i-1][j]
            else:
                r=self.solve(s,t,i-1,j)
            self.p[i][j]=l+r
        else:
            self.p[i][j]=self.solve(s,t,i-1,j)
        return self.p[i][j]
















        # n=len(s)+1
        # m=len(t)+1
        # tb=[[None]*m for i in range(n)]
        # for i in range(n):
        #     for j in range(m):
        #         if i==0 or j==0:
        #             tb[i][j]=0
        # for i in range(1,n):
        #     for j in range(1,m):
        #         if s[i-1]==t[j-1] and i!=j:
        #             tb[i][j]=1+tb[i-1][j-1]
        #         else:
        #             tb[i][j]=max(tb[i-1][j],tb[i][j-1])
        # print(tb)
        # return len(s)-tb[n-1][m-1]

        