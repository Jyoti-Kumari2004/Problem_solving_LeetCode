class Solution:
    def __init__(self):
        self.t=[[[[[None]*2 for i in range(2)]for j in range(1024)]for k in range(2)] for l in range(10)]

    def numDupDigitsAtMostN(self, n: int) -> int:
        mask=0000000000
        return self.solve(0,1,mask,False,str(n),False)
    def solve(self,ind,tight,mask,repeated,s,started):
        if ind==len(s):
            if repeated and started:
                return 1
            else:
                return 0
        if ind>len(s):
            return 0
        if self.t[ind][tight][mask][repeated][started]:
            return self.t[ind][tight][mask][repeated][started]
        newlimit=9 if tight==0 else int(s[ind])
        res=0
        
        for i in range(newlimit+1):
            newtight= 1 if (tight==1 and i==int(s[ind])) else 0
            if started==False and i==0:
                res+=self.solve(ind+1,newtight,mask,False,s,False)
            else:
                indi=-1
                newmask=mask
                if (mask & (1 << i)):
                    newrepeated=True
                else:
                    if repeated==True:
                        newrepeated=True
                    else:
                        indi=-2
                        newrepeated=False
                    newmask = mask | (1 << i)
                res+=self.solve(ind+1,newtight,newmask,newrepeated,s,True)
        self.t[ind][tight][mask][repeated][started]=res
        return res

    
        
        