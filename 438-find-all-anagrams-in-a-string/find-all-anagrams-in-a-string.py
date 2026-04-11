class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        bit=[0]*26
        for ch in p:
            bit[ord(ch)-ord('a')]+=1
        i,j=0,0
        sample=[0]*26
        size=len(p)
        curr=0
        ans=[]
        while j<len(s):
            sample[ord(s[j])-ord('a')]+=1
            curr+=1
            if curr>size:
                if sample[ord(s[i])-ord('a')]>0:
                    sample[ord(s[i])-ord('a')]-=1
                i+=1
                curr-=1
            if sample==bit and curr==size:
                ans.append(i)
            j+=1
        return ans
            


        