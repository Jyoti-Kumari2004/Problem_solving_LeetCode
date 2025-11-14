class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def line(arr):
            prev = curr = 0
            for v in arr:
                prev, curr = curr, max(curr, prev + v)
            return curr

        return max(line(nums[1:]), line(nums[:-1]))
