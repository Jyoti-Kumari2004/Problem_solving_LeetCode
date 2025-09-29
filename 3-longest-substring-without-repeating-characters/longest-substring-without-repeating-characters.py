class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        m=0
        h=defaultdict(int)
        while j<len(s):
            h[s[j]]+=1
            if len(h)==(j-i+1):
                m=max(m,j-i+1)
            elif len(h)<j-i+1:
                h[s[i]]-=1
                if h[s[i]]==0:
                    h.pop(s[i])
                i+=1
            j+=1
        return m
       
        