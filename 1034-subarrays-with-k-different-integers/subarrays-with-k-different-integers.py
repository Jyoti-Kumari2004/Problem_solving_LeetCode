class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmostk(k,nums)-self.atmostk(k-1,nums)
    
    def atmostk(self,k,nums):
        d=defaultdict(int)
        i,j=0,0
        count=0
        while j<len(nums):
            d[nums[j]]+=1
            while len(d)>k:
                d[nums[i]]-=1
                if d[nums[i]]==0:
                    del d[nums[i]]
                i+=1
            count+=j-i+1
            j+=1
        return count