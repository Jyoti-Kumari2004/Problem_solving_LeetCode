class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans=None
        for i in range(len(nums)):
            if nums[i]!=i:
                if ans==None:
                    ans=i
                else:
                    ans&=i
        if ans==None:
            return 0
        return ans
        