class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        d=defaultdict(int)
        for ch in t:
            d[ch]+=1
        count=len(d)
        bi=0
        bj=0
        i=0
        j=0
        ans=float('inf')
        while j<len(s):
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]]==0:
                    count-=1
            while count==0:
                if j-i+1<ans:
                    bi=i
                    bj=j
                    ans=j-i+1
                if s[i] in d:
                    d[s[i]]+=1
                    if d[s[i]]==1:
                        count+=1
                i+=1
            j+=1
        if ans==float('inf'):
            return ""
        return s[bi:bj+1]

        