class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        flag=False
        ans=[0]*len(nums)
        oc=0
        for num in nums:
            
            if num!=0:
                pro*=num
            else:
                flag=True
                oc+=1
            if oc>1:
                return [0]*len(nums)
        for i in range(len(nums)):
            if flag==True:
                if nums[i]!=0:
                    ans[i]=0
                elif nums[i]==0:
                    ans[i]=pro
            else:
                ans[i]=pro//nums[i]
        return ans
        