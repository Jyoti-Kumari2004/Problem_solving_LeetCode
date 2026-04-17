class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        d=defaultdict(int)
        ans=float('inf')
        for i in range(len(nums)):
            x=int(str(nums[i])[::-1])
            if nums[i] in d:
                ans=min(ans,abs(i-d[nums[i]]))
            d[int(x)]=i
        if ans==float('inf'):
            return -1
        return ans


        