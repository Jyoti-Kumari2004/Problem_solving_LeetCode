class Solution:
    def beautySum(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            d=defaultdict(int)
            mini=500
            maxi=0
            for j in range(i,len(s)):
                d[s[j]]+=1
                mini=min(d.values())
                maxi=max(d.values())
                if len(d)>1:
                    ans+=maxi-mini
        return ans
            