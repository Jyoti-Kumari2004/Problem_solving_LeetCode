class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        d1=set()
        d2=set()
        for i in nums1:
            d1.add(i)
        for j in nums2:
            d2.add(j)
        print(d1,d2)
        ans=[]
        n=[]
        for num in d1:
            if num not in d2:
                n.append(num)
        ans.append(n)
        n=[]
        for num in d2:
            if num not in d1:
                n.append(num)
        ans.append(n)
        return ans