class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=defaultdict(int)
        ans=0
        count=0
        i=0
        j=0
        while j<len(s):
            if s[j] not in d:
                count+=1
                d[s[j]]+=1
                ans=max(ans,len(d))
                print(s[j])
            else:
                while s[j] in d:
                    d[s[i]]-=1
                    count-=1
                    if d[s[i]]==0:
                        d.pop(s[i])
                    i+=1
                d[s[j]]+=1
            j+=1
        return ans
                

            

        