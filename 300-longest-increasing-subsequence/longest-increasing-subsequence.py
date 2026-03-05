class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp=[]
        temp.append(nums[0])
        for i in range(len(nums)):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                ind=self.lower_bound(temp,nums[i])
                temp[ind]=nums[i]
        return len(temp)
    
    def lower_bound(self, arr, target):
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] < target:
                l = m + 1
            else:
                r = m
        return l

        