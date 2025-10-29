class Solution:
    def findMin(self, arr: List[int]) -> int:
        n=len(arr)
        s=0
        e=n-1
        if n==1:
            return arr[0]
        while s<=e:
            mid=s+(e-s)//2
            if mid<n-2 and arr[mid]>arr[mid+1]:
                return arr[mid+1]
            elif mid>=1 and arr[mid]<arr[mid-1]:
                return arr[mid]
            elif arr[mid]>=arr[s]:
                s=mid+1
            else:
                e=mid-1
        return arr[0]