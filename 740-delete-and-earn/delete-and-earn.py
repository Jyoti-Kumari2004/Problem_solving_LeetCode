class Solution:
    def __init__(self):
        self.t=[-1]*10001
    def deleteAndEarn(self, nums: list[int]) -> int:
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        mini=min(nums)
        maxi=max(nums)
        return self.solve(mini,d,mini,maxi)
    def solve(self,curr,d,mini,maxi):
        if curr>maxi:
            return 0
        if curr<mini:
            return 0
        if self.t[curr]!=-1:
            return self.t[curr]
        ch1=curr*d[curr]+self.solve(curr+2,d,mini,maxi)
        ch2=self.solve(curr+1,d,mini,maxi)
        self.t[curr]=max(ch1,ch2)
        return max(ch1,ch2)