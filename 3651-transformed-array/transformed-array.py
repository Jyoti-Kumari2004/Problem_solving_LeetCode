class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(nums[(nums[i]+i)%n])
            elif nums[i]<0:
                res.append(nums[(((i-abs(nums[i]))%n)+n)%n])
            else:
                res.append(nums[i])
        return res

        