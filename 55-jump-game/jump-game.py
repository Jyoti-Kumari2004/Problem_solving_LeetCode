class Solution:
    def __init__(self):
        self.t=[-1 for i in range(10001)]
    def canJump(self, nums: List[int]) -> bool:
        # return self.solve(nums,0)
        #using greedy method:
        maxInd=0
        j=0
        while j<len(nums):
            if j>maxInd:
                return False
            maxInd=max(maxInd,nums[j]+j)
            if maxInd==len(nums)-1:
                return True
            j+=1
            
        return True






    #1.using dp and recurrsion , the complexity is O(n**2) and space is O(10001)
    # def solve(self,nums,ind):
    #     if ind==len(nums)-1:
    #         return True
    #     if ind>len(nums)-1:
    #         return False
    #     if self.t[ind]!=-1:
    #         return self.t[ind]
    #     res=False
    #     for i in range(1,nums[ind]+1):
    #         if self.solve(nums,ind+i)==True:
    #             res=True
    #             break
    #     self.t[ind]=res
    #     return self.t[ind]
            
        


        