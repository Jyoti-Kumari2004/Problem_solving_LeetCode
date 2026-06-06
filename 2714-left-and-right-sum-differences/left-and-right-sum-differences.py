class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=[]
        r=[0]*len(nums)
        s=0
        for i in range(len(nums)):
            
            l.append(s)
            s+=nums[i]
        s=0
        for i in range(len(nums)-1,-1,-1):
            
            r[i]=s
            s+=nums[i]
        sol=[]
        for i in range(len(nums)):
            sol.append(abs(l[i]-r[i]))
        return sol
        