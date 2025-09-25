class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)

        leftmax=[0]*(n)
        rightmax=[0]*(n)

        leftmax[0]=height[0]
        rightmax[n-1]=height[-1]

        for i in range(len(height)):
            leftmax[i]=max(height[i],leftmax[i-1])

        for i in range(len(height)-2,-1,-1):
            rightmax[i]=max(height[i],rightmax[i+1])

        sum=0
        for i in range(len(height)):
            if height[i]<leftmax[i] and height[i]<rightmax[i]:
                sum+=min(leftmax[i],rightmax[i])-height[i]
        return sum