class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # the below solution is having complexity O(n) we can optimize this more byt suing binary search in the next solution

        # i=0
        # j=0
        # na=[]
        # while i<len(nums1) and j<len(nums2):
        #     if nums1[i]<=nums2[j]:
        #         na.append(nums1[i])
        #         i+=1
        #     elif nums1[i]>nums2[j]:
        #         na.append(nums2[j])
        #         j+=1
        
        # while j<len(nums2):
        #     na.append(nums2[j])
        #     j+=1
        # while i<len(nums1):
        #     na.append(nums1[i])
        #     i+=1
        # print(na)
        # if len(na)%2!=0:
        #     return na[len(na)//2]
        # else:
        #     m1=(len(na)//2)-1
        #     m2=m1+1
        #     return (na[m1]+na[m2])/2

        #here is the solution using binary search in O(log n) complexity, optimized one
        n1=len(nums1)
        n2=len(nums2)
        if n1>n2:
            return self.findMedianSortedArrays(nums2,nums1)
        s=0
        e=n1
        l=(n1+n2+1)//2
        
        while s<=e:
            #these l1,l2,r1,r2 are written inside the loop because purani values change nhi ho rhi har bar...to ab change hogi i mean reset hogi
            l1,l2=float('-inf'),float('-inf')
            r1,r2=float('inf'),float('inf')
            mid1=s+(e-s)//2
            mid2=l-mid1
            if mid1-1>=0:
                l1=nums1[mid1-1]
            if mid2-1>=0:
                l2=nums2[mid2-1]
            if mid1<n1:
                r1=nums1[mid1]
            if mid2<n2:
                r2=nums2[mid2]

            if l1<=r2 and l2<=r1:
                if (n1+n2)%2==1:
                    return max(l1,l2)
                ls=max(l1,l2)
                rs=min(r1,r2)
                return (ls+rs)/2
            elif l1>r2:
                e=mid1-1
            else:
                s=mid1+1

        return 0