class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        self.solve(s,wordDict,0,[],res)
        ans=[]
        for lis in res:
            ans.append(" ".join(lis))
            
        return ans
        # return " ".join(res)

    def solve(self,s,wordDict,ind,path,res):
        if ind==len(s):
            res.append(path.copy())
            return 
        for i in range(ind,len(s)+1):
            if s[ind:i+1] in wordDict:
                path.append(s[ind:i+1])
                self.solve(s,wordDict,i+1,path,res)
                path.pop()
