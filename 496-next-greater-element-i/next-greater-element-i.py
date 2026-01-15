class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d=defaultdict(int)
        s=[]
        j=len(nums2)-1
        s.append(-1)
        for i in range(len(nums2)-1,-1,-1):

            if s and s[-1]>nums2[i]: 
                d[nums2[i]]=s[-1] 
                s.append(nums2[i])
                
            else:
                while s and s[-1]<nums2[i]: 
                    s.pop()
                if not s:
                    d[nums2[i]]=-1
                else:
                    d[nums2[i]]=s[-1]
                s.append(nums2[i])
        res=[]
        for i in range(len(nums1)):
            res.append(d[nums1[i]])
        return res
        

        