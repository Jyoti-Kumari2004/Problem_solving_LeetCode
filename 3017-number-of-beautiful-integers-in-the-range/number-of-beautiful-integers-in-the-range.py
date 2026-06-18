class Solution:
    def __init__(self):
        self.t=[]
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        self.t=[[[[[[None]*3 for i in range(10)] for j in range(10)]for c in range(21)] for x in range(3)] for m in range(len(str(high)))]
        h=self.solve(0,1,0,k,0,0,str(high),False)
        self.t=[[[[[[None]*3 for i in range(10)] for j in range(10)]for c in range(21)] for x in range(3)] for m in range(len(str(low-1)))]
        l=self.solve(0,1,0,k,0,0,str(low-1),False)
        return h-l
        # else:
        #     return h
    def solve(self,ind,tight,mod,k,ev,odd,s,started):
        if ind==len(s):
            if mod==0 and ev==odd and started==True:
                return 1
            else:
                return 0
        if ind>len(s):
            return 0
        newlimit =9 if tight==0 else int(s[ind])
        res=0
        if self.t[ind][tight][mod][ev][odd][started]!=None:  
            return self.t[ind][tight][mod][ev][odd][started]
        for i in range(newlimit+1):
            newtight= 1 if tight==1 and i==int(s[ind]) else 0
            if not started and i==0:
                res+=self.solve(ind+1,newtight,0,k,0,0,s,False)
            else:
                newev=ev+(1 if i%2==0 else 0)
                newodd=odd+(1 if i%2!=0 else 0)
                newmod = (mod * 10 + i) % k
                res+=self.solve(ind+1,newtight,newmod,k,newev,newodd,s,True) 
        self.t[ind][tight][mod][ev][odd][started]=res
        return res
            
