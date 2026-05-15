class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for num in nums:
            st=str(num)
            ans.extend(list(map(int,list(st))))
        return ans
        