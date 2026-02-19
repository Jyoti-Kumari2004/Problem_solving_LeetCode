class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        self.solve(s,0,res,[])
        return res

    def solve(self,s,ind,res,path):
        if ind==len(s):
            res.append(path.copy())
            return 
        for i in range(ind,len(s)):
            if self.isPanil(s[ind:i+1])==True:
                path.append(s[ind:i+1])
                self.solve(s,i+1,res,path)
                path.pop()
        
    def isPanil(self,s):
        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True
