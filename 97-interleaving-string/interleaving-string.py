class Solution:
    def __init__(self):
        self.t = [[[-1]*(201) for _ in range(101)] for _ in range(101)]
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.solve(len(s1),len(s2),len(s3),s1,s2,s3)

    def solve(self,i,j,n,s,t,x):
        if i==0 and j==0 and n==0:
            return True
        elif n==0 or (i==0 and j==0):
            return False
        elif i==0 and n!=0:
            if x[0:n]!=t[0:j]:
                return False
            return True
        elif j==0:
            if x[0:n]!=s[0:i]:
                return False
            return True
        if self.t[i][j][n]!=-1:
            return self.t[i][j][n]
        if x[n-1]==s[i-1] and x[n-1]==t[j-1]:
            self.t[i][j][n]=self.solve(i-1,j,n-1,s,t,x) or self.solve(i,j-1,n-1,s,t,x)
        elif x[n-1]==s[i-1]:
            self.t[i][j][n]= self.solve(i-1,j,n-1,s,t,x)
        elif x[n-1]==t[j-1]:
            self.t[i][j][n]= self.solve(i,j-1,n-1,s,t,x)
        else:
            self.t[i][j][n]= False
        return self.t[i][j][n]

        
        