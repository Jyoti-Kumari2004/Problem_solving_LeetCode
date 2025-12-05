class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        tot=sum(nums)
        curr_sum=0
        count=0
        for i in range(0,len(nums)):
            curr_sum+=nums[i]
            if abs(curr_sum-(tot-curr_sum))%2==0:
                count+=1
        if count==0:
            return 0
        return count-1
            


        