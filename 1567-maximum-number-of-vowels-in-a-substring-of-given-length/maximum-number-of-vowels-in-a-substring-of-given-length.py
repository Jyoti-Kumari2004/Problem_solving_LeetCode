class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        d=defaultdict(int)
        j,i=0,0
        ans=0
        count=0
        while j<len(s):
            if s[j] in "aeiou":
                d[s[i]]+=1
                count+=1
            
            if j-i+1>k:
                if s[i] in "aeiou":
                    d[s[i]]-=1
                    if d[s[i]]==0:
                        del d[s[i]]
                    count-=1
                i+=1
            if j-i+1==k:
                ans=max(ans,count)
            j+=1
        return ans
