class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k<arr[0]:
            return k
        if k>arr[-1]:
            return k+len(arr)
        new=[]
        for i in range(len(arr)):
            new.append(arr[i]-(i+1))
        print(new)
        s=0
        e=len(new)-1
        while s<=e:
            mid=s+(e-s)//2
            if new[mid]<k:
                s=mid+1
            else:
                e=mid-1
        print(s,e)
        return k-new[e]+arr[e]
        
        