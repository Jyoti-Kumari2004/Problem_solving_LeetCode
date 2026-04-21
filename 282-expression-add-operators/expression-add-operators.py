class Solution:
    def __init__(self):
        self.res=[]
    def addOperators(self, num: str, target: int) -> List[str]:
        self.res=[]
        self.solve(0,"",target,num,0,0)
        return self.res
    def solve(self,ind,path,target,s,eval,resi):
        if ind==len(s):
            if eval==target:
                self.res.append(path)
            return 
        currStr=""
        for i in range(ind,len(s)):
            if i>ind and s[ind]=="0":
                return 
            currStr+=s[i]
            if ind==0:
                self.solve(i+1,path+currStr,target,s,int(currStr),int(currStr))
            else:
                self.solve(i+1,path+"+"+currStr,target,s,eval+int(currStr),int(currStr))
                self.solve(i+1,path+"-"+currStr,target,s,eval-int(currStr),-int(currStr))
                self.solve(i+1,path+"*"+currStr,target,s,(eval-resi)+(resi*int(currStr)),resi*int(currStr))

        