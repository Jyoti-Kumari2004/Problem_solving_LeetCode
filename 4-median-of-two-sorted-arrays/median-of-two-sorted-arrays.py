class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        na=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                na.append(nums1[i])
                i+=1
            elif nums1[i]>nums2[j]:
                na.append(nums2[j])
                j+=1
        
        while j<len(nums2):
            na.append(nums2[j])
            j+=1
        while i<len(nums1):
            na.append(nums1[i])
            i+=1
        print(na)
        if len(na)%2!=0:
            return na[len(na)//2]
        else:
            m1=(len(na)//2)-1
            m2=m1+1
            return (na[m1]+na[m2])/2

