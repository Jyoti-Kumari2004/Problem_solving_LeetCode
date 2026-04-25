class Solution:
    def reverseVowels(self, s: str) -> str:
        ls=[]
        for ch in s:
            if ch in "aeiouAEIOU":
                ls.append(ch)
        ls=ls[::-1]
        ans=""
        i=0
        for ch in s:
            if ch in "aeiouAEIOU":
                ans+=ls[i]
                i+=1
            else:
                ans+=ch
        return ans
            