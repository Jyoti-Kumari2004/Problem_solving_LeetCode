class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            d=defaultdict(int)
            for j in range(i,len(nums)):
                d[nums[j]]+=1
                ans+=len(d)**2
        return ans

