class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]]+=1
        for j in d:
            if d[j]>=len(nums)//2:
                return j
        return -1