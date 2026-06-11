class Solution:
    def __init__(self):
        self.t=[[[-1]*401 for j in range(2)]for i in range(23)]

    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        self.t=[[[-1]*401 for j in range(2)]for i in range(23)]
        one=self.solve(0,1,num2,0,min_sum,max_sum)%1000000007
        n1=int(num1)
        self.t=[[[-1]*401 for j in range(2)]for i in range(23)]
        two=self.solve(0,1,str(n1-1),0,min_sum,max_sum)%1000000007
        print(one)
        print(two)
        return (one-two)%1000000007
    #@lru_cache(None) # we can use this also, ..but i will also implement proper memoizaiton not the inbuilt things

    def solve(self,ind,tight,s,curr,mini,maxi):
        if curr>maxi:
            return 0
        if ind==len(s):
            return 1 if (mini<=(curr)<=maxi) else 0
        if tight==0:
            newlimit=9
        else:
            newlimit=int(s[ind])
        if self.t[ind][tight][curr]!=-1:
            return self.t[ind][tight][curr]
        res=0
        for i in range(newlimit+1):
            newtight=1 if (i==int(s[ind]) and tight==1) else 0
            res+=self.solve(ind+1,newtight,s,curr+i,mini,maxi)
        self.t[ind][tight][curr]=res
        return res
        

            