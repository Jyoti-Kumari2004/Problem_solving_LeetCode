class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        j=1
        i=0
        res=[]
        while j<len(nums)+1:
            count=0
            while j<len(nums) and nums[j]-nums[j-1]==1:
                count+=1
                j+=1
            if count>0:
                res.append(f"{nums[i]}->{nums[j-1]}")
            else:
                res.append(str(nums[j-1]))
            i=j
            j+=1
        return res
            


        