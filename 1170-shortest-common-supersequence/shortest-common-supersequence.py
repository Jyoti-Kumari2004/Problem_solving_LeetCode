class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1)+1
        m=len(str2)+1
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    t[i][j]=0
        for i in range(1,n):
            for j in range(1,m):
                if str1[i-1]==str2[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        i=n-1
        j=m-1
        ans=""
        while i>0 and j>0:
            if str1[i-1]==str2[j-1]:
                ans+=str1[i-1]
                i-=1
                j-=1
            elif t[i-1][j]<t[i][j-1]:
                ans+=str2[j-1]
                j-=1
            else:
                ans+=str1[i-1]
                i-=1
        while i>0:
            ans+=str1[i-1]
            i-=1
        while j>0:
            ans+=str2[j-1]
            j-=1
        return ans[::-1]