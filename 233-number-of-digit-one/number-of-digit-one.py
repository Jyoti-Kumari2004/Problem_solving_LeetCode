class Solution:
    def countDigitOne(self, n: int) -> int:
        return self.solve(0,1,0,str(n))
    @lru_cache(None)
    def solve(self,ind,tight,c,s):
        if ind==len(s):
            return c
        if tight==1:
            newlimit=int(s[ind])
        else:
            newlimit=9
        res=0
        for i in range(newlimit+1):
            upc=c+(1 if i==1 else 0)
            newtight=1 if (i==int(s[ind]) and tight==1) else 0
            res+=self.solve(ind+1,newtight,upc,s)
        return res
        