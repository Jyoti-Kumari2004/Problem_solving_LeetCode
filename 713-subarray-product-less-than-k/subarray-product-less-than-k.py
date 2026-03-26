class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        count=0
        pro=1
        while j<len(nums):
            pro*=nums[j]
            
            while pro>=k and i<j:
                pro//=nums[i]
                i+=1
            if pro<k:
                count+=j-i+1
            j+=1

        return count

        