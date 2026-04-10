class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        m=len(s)
        t=[[False]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==j:
                    t[i][j]=True
        for i in range(n-1,-1,-1):
            for j in range(m):
                if j>i:
                    l=j-i+1
                    if l==2 and s[i]==s[j]:
                        t[i][j]=True
                    elif l==3 and s[i]==s[j]:
                        t[i][j]=True
                    else:
                        if s[i]==s[j] and t[i+1][j-1]:
                            t[i][j]=True
                        else:
                            t[i][j]=False
        count=0
        for i in range(n):
            for j in range(m):
                if t[i][j]==True:
                    count+=1
        return count

        



        