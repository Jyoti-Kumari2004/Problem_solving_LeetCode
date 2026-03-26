class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]
        for k in range(len(nums)-2):
            if k>0 and nums[k]==nums[k-1]:
                continue
            t=0-nums[k]
            i=k+1
            j=len(nums)-1
            while i<j:
                if nums[i]+nums[j]==t:
                    ans.append((nums[k],nums[i],nums[j]))
                    i+=1
                    j-=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
                elif nums[i]+nums[j]<t:
                    i+=1
                else:
                    j-=1
        return ans


         