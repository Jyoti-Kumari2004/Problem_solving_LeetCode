class Solution:
    def prefixSum(self,arr):
        new_arr=[]
        
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,0
        sum=0
        m=float('inf')
        while j<len(nums):
            sum+=nums[j]
            
            while sum>=target:
                m=min(m,j-i+1)
                sum-=nums[i]
                i+=1
                
            j+=1
        
        if m==float('inf'):
            return 0
        else:
            return m