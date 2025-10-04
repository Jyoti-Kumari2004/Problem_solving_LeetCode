class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        li=[]
        ans=[]
        i,j=0,0
        while j<len(nums):
            if  len(li)==0 or nums[j]<li[-1]:
                li.append(nums[j])
            else:
                while li and nums[j]>li[-1] : 
                    li.pop()
                li.append(nums[j])
            
            if k==j-i+1:
                if len(li)==0:
                    ans.append(0)
                else:
                    ans.append(li[0])
                if nums[i]==li[0]:
                    li.pop(0)
                i+=1
            j+=1
        return ans

                