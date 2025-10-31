class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        h=defaultdict(int)
        ans=[]
        for i in range(len(nums)):
            if h[nums[i]]!=0:
                ans.append(nums[i])
            else:
                h[nums[i]]+=1
        return ans
        
