class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j,z,m=0,0,0,0
        while j<len(nums):
            if nums[j]==0:
                z+=1
            if z<=k:
                m=max(m,j-i+1)
            if z>k:
                while z>k:
                    if nums[i]==0: 
                        z-=1
                    i+=1
            j+=1
        return m