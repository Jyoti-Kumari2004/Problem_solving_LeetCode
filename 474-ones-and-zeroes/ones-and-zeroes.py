class Solution:
    def __init__(self):
        self.t={}
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        return self.solve(0,strs,m,n,0,0)
        return self.ans
    def solve(self,ind,strs,m,n,currm,currn):
        if ind>=len(strs):
            return 0
        if currm>m or currn>n:
            return 0
        if (ind,currm,currn) in self.t:
            return self.t[(ind,currm,currn)]
        st=strs[ind]
        mi,ni=0,0
        for chr in list(st):
            if chr=="0":
                mi+=1
            if chr=="1":
                ni+=1
        ch=0
        if currm+mi<=m and currn+ni<=n:
            ch=1+self.solve(ind+1,strs,m,n,currm+mi,currn+ni)
        ch1=self.solve(ind+1,strs,m,n,currm,currn)
        self.t[(ind,currm,currn)]=max(ch1,ch)
        return max(ch1,ch)