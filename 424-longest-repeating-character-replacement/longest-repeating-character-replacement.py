class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d= defaultdict(int)
        j=0
        i=0
        max_freq=0
        ans=float('-inf')
        while j<len(s):
            d[s[j]]+=1
            max_freq=max(max_freq,d[s[j]])
    
            while (j-i+1)-max_freq>k:
                d[s[i]]-=1
                max_freq=max(d.values())
                i+=1
                
            if ((j-i+1)-max_freq)<=k:
                ans=max(ans,j-i+1)
            
            j+=1
        return ans
        