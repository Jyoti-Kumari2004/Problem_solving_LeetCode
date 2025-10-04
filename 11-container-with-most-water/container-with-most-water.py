class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        lm,rm=0,0
        ans=0
        m=0
        j=len(height)-1
        while i<j:
            lm=max(lm,height[i])
            rm=max(rm,height[j])
            ans=min(lm,rm)*(j-i)
            m=max(m,ans)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
            
        return m
        