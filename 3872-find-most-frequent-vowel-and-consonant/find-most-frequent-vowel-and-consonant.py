class Solution:
    def maxFreqSum(self, s: str) -> int:
        h=defaultdict(int)
        for i in s:
            h[i]+=1
        maxv,maxc=0,0
        for j in h:
            if j in "aeiouAEIOU":
                if maxv<h[j]:
                    maxv=h[j]
            else:
                if maxc<h[j]:
                    maxc=h[j]
        return maxc+maxv
            


        