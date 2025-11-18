class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        
        for i in range(len(nums)):
            if nums[i]==1:
                break
        a=i
        j=i
        while j<len(nums):
            if nums[j]==1 and i!=j:
                if j-i-1<k:
                    return False
                i=j
            j+=1
        return True

                
        