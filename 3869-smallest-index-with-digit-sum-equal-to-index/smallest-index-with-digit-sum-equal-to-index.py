class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i==self.sumd(str(nums[i])):
                return i
        return -1

    def sumd(self,num):
        s=0
        for ch in num:
            s+=int(ch)
        return s
        