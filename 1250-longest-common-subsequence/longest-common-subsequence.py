#Top down approach
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)+1
        m=len(text2)+1
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    t[i][j]=0 
        for i in range(1,n):
            for j in range(1,m):
                if text1[i-1]==text2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[n-1][m-1]




#Memoization/bottom up approach 
    # class Solution:
    #     def __init__(self):
    #         self.t=[[-1]*1001 for i in range(1002)]
    #     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #         n=len(text1)
    #         m=len(text2)
    #         return self.LCS(text1,text2,n,m)

    #     def LCS(self,X,Y,n,m):
    #         if n==0 or m==0:
    #             return 0
    #         if self.t[n][m]!=-1:
    #             return self.t[n][m]
    #         elif X[n-1]==Y[m-1]:
    #             self.t[n][m]=1+self.LCS(X,Y,n-1,m-1)
    #         else:
    #             self.t[n][m]= max(self.LCS(X,Y,n-1,m),self.LCS(X,Y,n,m-1))

    #         return self.t[n][m]

#recursive approach:
    # class Solution:
    #     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #         return self.LCS(text1,text2,len(text1),len(text2))

    #     def LCS(self,X,Y,n,m):
    #         if n==0 or m==0:
    #             return 0
    #         elif X[n-1]==Y[m-1]:
    #             return 1+self.LCS(X,Y,n-1,m-1)
    #         else:
    #             return max(self.LCS(X,Y,n-1,m),self.LCS(X,Y,n,m-1))