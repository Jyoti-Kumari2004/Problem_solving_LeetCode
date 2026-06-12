class Solution:
    def __init__(self):
        self.t=[[[[None]*3 for i in range(10)]for i in range(2)]for i in range(101)]
    def countSteppingNumbers(self, low: str, high: str) -> int:
        l=self.solve(0,1,0,str(int(low)-1),False)%1000000007
        self.t=[[[[None]*3 for i in range(10)]for i in range(2)]for i in range(101)]
        r=self.solve(0,1,0,high,False)%1000000007
        return (r-l)%1000000007
    
    def solve(self,ind,tight,prev,s,started):
        if ind==len(s):
            if started:
                return 1
            else:
                return 0
        if self.t[ind][tight][prev][started]!=None:
            return self.t[ind][tight][prev][started]
        newlimit=9 if tight==0 else int(s[ind])
        res=0
        for i in range(newlimit+1):
            newtight= 1 if( i==int(s[ind]) and tight==1) else 0
            if started==False : 
                if i==0:
                    res+=self.solve(ind+1,newtight,0,s,False)
                else:
                    res+=self.solve(ind+1,newtight,i,s,True)
            elif abs(prev-i)==1:
                res+=self.solve(ind+1,newtight,i,s,True)
        self.t[ind][tight][prev][started]=res
        return res
        