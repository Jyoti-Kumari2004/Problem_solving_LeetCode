class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        temp=[]
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        self.helper(res,temp,nums,d)
        return res

    def helper(self,res,temp,nums,d):
        if len(temp)==len(nums):
            res.append(temp.copy())
            return 
        for num in d:
            if d[num]==0:
                continue
            temp.append(num)
            d[num]-=1
            self.helper(res,temp,nums,d)
            temp.pop()
            d[num]+=1