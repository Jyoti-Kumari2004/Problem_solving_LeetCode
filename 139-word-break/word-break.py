class Solution:
    def __init__(self):
        self.memo={}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.solve(s,0,wordDict)

        
    def solve(self,s,ind,wordDict):
        if ind==len(s):
            return True
        if ind in self.memo:
            return self.memo[ind]
        for i in range(ind,len(s)):
            if self.isValid(s[ind:i+1],wordDict)==True:
                if self.solve(s,i+1,wordDict):
                    self.memo[ind]=True
                    return True
        self.memo[ind]=False
        return False
    def isValid(self,s,dictt):
        if s in dictt:
            return True
        return False
