class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        i=0
        while i<len(nums):
            if nums[i]==1:
                i+=2
            else:
                left= True if i==0 or nums[i-1]!=1 else False
                right= True if i==len(nums)-1 or nums[i+1]!=1 else False
                if right and left:
                    n-=1
                    i+=2
                else:
                    i+=1
        if n>0:
            return False
        return True