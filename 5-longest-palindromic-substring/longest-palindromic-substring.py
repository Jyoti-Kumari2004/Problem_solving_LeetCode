class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=[]
        n=len(s)
        m=len(s)
        max_i=0
        max_j=0
        pt=[[False]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==j:
                    pt[i][j]=True
        for i in range(n-1,-1,-1):
            for j in range(m):
                if j>i:
                    l=j-i+1
                    if s[i]==s[j]:
                        if l==2 or l==3:
                            pt[i][j]=True
                        else:
                            if pt[i+1][j-1]:
                                pt[i][j]=True
                            else:
                                pt[i][j]=False
                    else:
                        pt[i][j]=False
        ans=0
        for i in range(n):
            for j in range(m):
                if pt[i][j]==True:
                    if ans<j-i:
                        max_j=j
                        max_i=i
                        ans=j-i
                    ans=max(ans,j-i)
        return s[max_i:max_j+1]


    # def lcs(self,s1,s2):
    #     n=len(s1)+1
    #     m=len(s2)+1
    #     ans=0
    #     max_ind=0
    #     t=[[None]*m for i in range(n)]
    #     for i in range(n):
    #         for j in range(m):
    #             if i==0 or j==0:
    #                 t[i][j]=0
    #     res=[]
    #     for i in range(1,n):
    #         for j in range(1,m):
    #             if s1[i-1]==s2[j-1]:
    #                 t[i][j]=1+t[i-1][j-1]
    #                 if ans<t[i][j]:
    #                     max_ind=i-1
    #                     ans=t[i][j]
    #             else:
    #                 res=[]
    #                 t[i][j]=0
    #     start=max_ind-ans+1
    #     end=max_ind+1
    #     res=[]
    #     res.append(s1[start:end])
    #     return res
        