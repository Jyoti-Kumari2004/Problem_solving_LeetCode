class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        
        ans=0
        for numm in s:
            if numm-1 not in s:
                count=0
                num=numm
                i=0
                while num+i in s:
                    count+=1
                    i+=1
                ans=max(count,ans)
        return ans
            

                
                
        