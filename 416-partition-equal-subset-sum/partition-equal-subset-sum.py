class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2==0:
            print("yahan se")
            return self.subsetSum(nums,s//2,len(nums))
        else:
            return False
    def subsetSum(self,arr,s,n):
        m=s+1
        n=n+1
        t=[[None]*m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0:
                    t[i][j]=False
                if j==0:
                    t[i][j]=True
        for i in range(1,n):
            for j in range(1,m):
                if arr[i-1]<=j:
                    t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
                else:
                    t[i][j]=t[i-1][j]
        print(t[n-1][m-1])
        return t[n-1][m-1]
        