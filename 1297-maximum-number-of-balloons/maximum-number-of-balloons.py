class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d=defaultdict(int)
        for ch in "balloon":
            d[ch]+=1
        print(d)
        dd=defaultdict(int)
        for ch in text:
            if ch in "balloon":
                dd[ch]+=1
        if len(dd)<len(d):
            return 0
        ans=float('inf')
        for key,value in dd.items():
            if value==0:
                return 0
            ans=min(ans,dd[key]//d[key])
        if ans==float('inf'):
            return 0
        return ans
        
        