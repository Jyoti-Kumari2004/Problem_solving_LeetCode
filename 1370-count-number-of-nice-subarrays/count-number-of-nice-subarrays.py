class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        i,j,o,ans,more=0,0,0,0,0
        while j<len(nums):
            if nums[j]%2!=0:
                o+=1
            if o>k:
                while o>k:
                    if nums[i]%2!=0:
                        o-=1
                    i+=1
                    more=0
            
            if o==k:
                while o==k:
                    if nums[i]%2!=0:
                        break
                    else:
                        more+=1
                    i+=1
                ans+=more+1
            
            j+=1
        return ans
                
            

        