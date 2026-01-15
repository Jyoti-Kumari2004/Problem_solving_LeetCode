class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        r=self.nextmins(heights)
        l=self.prevmins(heights)
        print(r,l)
        ans=0
        for i in range(len(heights)):
            h=heights[i]
            w=r[i]-l[i]-1
            ar=h*w
            ans=max(ar,ans)
        return ans

    def nextmins(self,nums2):
        s=[]
        j=len(nums2)-1
        # s.append(-1)
        ng=[0]*len(nums2)
        for i in range(len(nums2)-1,-1,-1):

            if s and nums2[s[-1]]<nums2[i]: 
                ng[i]=s[-1] 
                s.append(i)
                 
            else:
                while s and nums2[s[-1]]>=nums2[i]: 
                    s.pop()
                if not s:
                    ng[i]=len(nums2)
                else:
                    ng[i]=s[-1]
                s.append(i)
        return ng
    def prevmins(self,nums):
        s=[]
        # s.append(len(nums))
        ng=[0]*len(nums)
        for i in range(0,len(nums)):

            if s and nums[s[-1]]<nums[i]: 
                ng[i]=s[-1] 
                s.append(i)
                
            else:
                while s and nums[s[-1]]>=nums[i]: 
                    s.pop()
                if not s:
                    ng[i]=-1
                else:
                    ng[i]=s[-1]
                s.append(i)
        return ng

