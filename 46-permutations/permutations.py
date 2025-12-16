class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        self.helper(res,temp,nums)
        return res

    def helper(self,res,temp,nums):
        if len(temp)==len(nums):
            res.append(temp.copy())
            return 
        for num in nums:
            if num in temp:
                continue
            temp.append(num)
            self.helper(res,temp,nums)
            temp.pop()

        