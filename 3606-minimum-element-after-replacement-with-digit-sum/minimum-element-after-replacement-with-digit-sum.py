class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans=float('inf')
        for num in nums:
            st=str(num)
            s=0
            for ch in range(len(st)):
                s+=int(st[ch])
            ans=min(ans,s)
        return ans
        