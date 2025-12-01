class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        avg=sum(batteries)//n
        s=1
        e=avg
        ans=0
        while s<=e:
            mid=s+(e-s)//2
            if self.solve(n,mid,batteries):
                ans=mid
                s=mid+1
            else:
                e=mid-1
        return ans
    def solve(self,n,num,arr):
        sum=0
        for i in arr:
            sum+=min(num,i)
        return (num*n<=sum)



        