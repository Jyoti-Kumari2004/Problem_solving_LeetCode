class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # s=set(nums)
        # i=1
        # ans=[]
        # n=len(nums)
        # while i<=n:
        #     if i not in s:
        #         ans.append(i)
        #     i+=1
        # return ans
        i=0
        while i<len(nums):
            idx=nums[i]-1
            if nums[i] != nums[idx]:
                nums[i],nums[idx]=nums[idx],nums[i]
            else:
                i+=1
        print(nums)
        exp=1
        ans=[]
        for i in range(len(nums)):
            if nums[i]!=exp:
                ans.append(exp)
            exp+=1
        return ans

        
        