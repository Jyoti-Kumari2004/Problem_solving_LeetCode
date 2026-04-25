class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set(nums)
        i=1
        ans=[]
        n=len(nums)
        while i<=n:
            if i not in s:
                ans.append(i)
            i+=1
        return ans

        