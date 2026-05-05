class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d=defaultdict(int)
        ans=0
        for i in range(len(nums)):
            if d[k-nums[i]]>0:
                ans+=1
                d[k-nums[i]]-=1
            else:
                d[nums[i]]+=1
        return ans










        # nums.sort()
        # i=0
        # j=len(nums)-1
        # ops=0
        # while i<j:
        #     if nums[i]+nums[j]==k:
        #         ops+=1
        #         i+=1
        #         j-=1
        #     elif nums[i]+nums[j]<k:
        #         i+=1
        #     else:
        #         j-=1
        # return ops

        