class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref=[0]*len(nums)
        pref[0]=nums[0]
        for i in range(len(nums)):
            pref[i]=pref[i-1]+nums[i]
        print(pref)
        return self.atmostk(nums,goal,pref)-self.atmostk(nums,goal-1,pref)
        
    def atmostk(self,nums,k,pref):
        d=defaultdict(int)
        j=0
        curr_sum=0
        i=0
        count=0
        while j<len(nums):
            curr_sum+=nums[j]
            while i<=j and curr_sum>k :
                curr_sum-=nums[i]
                i+=1
            count+=j-i+1
            j+=1
        return count
            
        
        