class Solution:
    def reverseDegree(self, s: str) -> int:
        dd=defaultdict(int)
        for i in range(1,27):
            dd[chr(96+i)]=27-i
        ans=0
        for i in range(len(s)):
            ans+=dd[s[i]]*(i+1)
        return ans


        