class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # hash = {}
        
        # for num in nums:
        #     if num in hash:
        #         hash[num]+=1
        #     else:
        #         hash[num]=1
        # for num in nums:
        #     if hash[num]==1:
        #         return num
        # return -1
        res=nums[0]
        for i in range(1,len(nums)):
            res^=nums[i]
        return res

        