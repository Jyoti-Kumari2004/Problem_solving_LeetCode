class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n=len(s1)+1
        m=len(s2)+1
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or j==0:
                    t[i][j]=0
        for i in range(1,n):
            for j in range(1,m):
                if s1[i-1]==s2[j-1]:
                    t[i][j]=t[i-1][j-1]+ord(s1[i-1])
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        #this method is through backtracking which is too lengthy and heavy..we can solve this by saving max value of ascii into the table itself
        # i=n-1
        # j=m-1
        # ans=""
        # while i>0 and j>0:
        #     if s1[i-1]==s2[j-1]:
        #         ans+=s1[i-1]
        #         i-=1
        #         j-=1
  
        #     elif t[i-1][j]>t[i][j-1]:
        #         i-=1
        #     else:
        #         j-=1
        # lcs=ans
        # print(ans[::-1])
        lcs_sum=t[n-1][m-1]
        s1_sum=0
        s2_sum=0
        for y in range(len(s1)):
            s1_sum+=ord(s1[y])
        for z in range(len(s2)):
            s2_sum+=ord(s2[z])
        return (s1_sum+s2_sum)-(2*lcs_sum)

    
