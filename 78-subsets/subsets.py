class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        ps=(1<<n)# power set size
        for i in range(ps):
            lv=[]
            for j in range(n):
                if  ((i&(1<<j)))!=0:
                    lv.append(nums[j])
            res.append(lv)
        return res
        