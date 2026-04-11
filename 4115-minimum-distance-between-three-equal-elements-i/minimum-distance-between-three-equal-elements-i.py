class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        d=defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        ans=float('inf')
        for key,lis in d.items():
            if len(lis)>=3:
                for i in range(len(lis)-2):
                    a=lis[i]
                    b=lis[i+1]
                    c=lis[i+2]
                    cal=abs(a-b)+abs(b-c)+abs(c-a)
                    ans=min(ans,cal)
        if ans==float('inf'):
            return -1
        return ans
        