class Solution:
    def __init__(self):
        self.res=float('inf')
        
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n=len(nums)
        self.t=[[[None]*(n+1) for i in range(n+1)]for i in range(n+1)]
        return self.solve(0,nums,k,op1,op2)

    def solve(self,ind,nums,k,op1,op2):
        if ind==len(nums)-1:
            if op1 and op2:
                res=ceil((nums[ind])/2)
                if nums[ind]>=k:
                    res=ceil((nums[ind]-k)/2)
                
                return min((nums[ind]-k if nums[ind]>=k else float('inf')),ceil(nums[ind]/2),nums[ind],min(ceil(nums[ind]/2)-(k if ceil(nums[ind]/2)>=k else 0),res))
            elif op1:
                return ceil(nums[ind]/2)
            elif op2 and nums[ind]>=k:
                return nums[ind]-k
            else:
                return nums[ind]
        if ind>=len(nums):
            return 0

        if self.t[ind][op1][op2]!=None:
            return self.t[ind][op1][op2]

        ch1=float('inf')
        ch2=float('inf')
        ch4=float('inf')
        if op1>0 and op2>0:
            res=ceil((nums[ind])/2)
            if nums[ind]>=k:
                res=ceil((nums[ind]-k)/2)
            ch4=min(ceil(nums[ind]/2)-(k if ceil(nums[ind]/2)>=k else 0),res)+self.solve(ind+1,nums,k,op1-1,op2-1)
            

        if op1>0:
            ch1=ceil(nums[ind]/2)+self.solve(ind+1,nums,k,op1-1,op2)

        
        if op2>0 and nums[ind]>=k:
            ch2=nums[ind]-k+self.solve(ind+1,nums,k,op1,op2-1)

        ch3=nums[ind]+self.solve(ind+1,nums,k,op1,op2)

        self.t[ind][op1][op2]=min(ch2,ch1,ch3,ch4)
        
        return self.t[ind][op1][op2]


        