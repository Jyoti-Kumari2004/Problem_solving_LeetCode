class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        sm=n*(n+1)//2
        return sm-sum(nums)
        