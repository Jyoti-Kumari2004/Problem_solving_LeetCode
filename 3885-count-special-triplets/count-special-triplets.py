class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count=0
        mod = 10**9 + 7
        # while 0=<i<j<k<n:
        h=defaultdict(int)
        h1=defaultdict(int)
        for j in range(1,len(nums)):
            h[nums[j]]+=1
        h1[nums[0]]+=1
        for i in range(1,len(nums)):
            val=nums[i]
            h[val]-=1
            lv=val*2
            rv=val*2
            count+=(h1[lv]*h[rv])%mod
            h1[val]+=1
        return count%mod
            



            