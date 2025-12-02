class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # if s=="bbbaaaba":
        #     return False

        sd=defaultdict(int)
        td=defaultdict(int)
        res1,res2=[],[]
        for i in range(len(s)):
            sd[s[i]]+=1
            td[t[i]]+=1
            res1=sd.values()
            res2=td.values()
            if list(res1)!=list(res2):
                return False
        return list(res1)==list(res2)
        