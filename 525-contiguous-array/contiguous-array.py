class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d=defaultdict(int)
        d[0]=-1
        curr=0
        ans=0
        for i in range(len(nums)):
            if nums[i]==0:
                curr-=1
            else:
                curr+=1
            if curr in d:
                ans=max(ans,i-d[curr])
            else:
                d[curr]=i
        return ans


        
        