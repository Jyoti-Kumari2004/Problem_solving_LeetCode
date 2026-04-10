class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
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

        self.solve(0,s,pt,res,[])
        return res
    def solve(self,ind,s,pt,res,path):
        if ind==len(s):
            res.append(path.copy())
            return 
        for i in range(ind,len(s)):
            if pt[ind][i]:
                path.append(s[ind:i+1]) 
                self.solve(i+1,s,pt,res,path)
                path.pop()
        