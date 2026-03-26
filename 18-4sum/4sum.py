class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        nums.sort()
        for n in range(len(nums)-3):
            if n>0 and nums[n]==nums[n-1]:
                continue
            for k in range(n+1,len(nums)-2):
                if k>n+1 and nums[k]==nums[k-1]:
                    continue
                i=k+1
                j=len(nums)-1
                curr_t=target-nums[n]-nums[k]
                while i<j:
                    if nums[i]+nums[j]==curr_t:
                        ans.append([nums[n],nums[k],nums[i],nums[j]])
                        i+=1
                        j-=1
                        while i<j and nums[i]==nums[i-1]:
                            i+=1
                        while i<j and nums[j]==nums[j+1]:
                            j-=1
                    elif nums[i]+nums[j]<curr_t:
                        i+=1
                    else:
                        j-=1
        return ans
        