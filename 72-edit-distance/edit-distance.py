class Solution:
    def __init__(self):
        self.t=[[-1]*501 for i in range(501)]
    def minDistance(self, word1: str, word2: str) -> int:
        return self.solve(word1,word2,len(word1),len(word2))
        
    def solve(self,s1,s2,n,m):
        if n==0:
            return m
        if m==0:
            return n
        if self.t[n][m]!=-1:
            return self.t[n][m]
        if s1[n-1]==s2[m-1]:
            self.t[n][m]=self.solve(s1,s2,n-1,m-1)
        else:
            self.t[n][m]= 1+min(self.solve(s1,s2,n-1,m-1),self.solve(s1,s2,n,m-1),self.solve(s1,s2,n-1,m)) 
        return self.t[n][m]    