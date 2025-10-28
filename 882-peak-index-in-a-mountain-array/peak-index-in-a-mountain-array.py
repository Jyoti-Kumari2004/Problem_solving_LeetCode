class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        s=0
        e=n-1
        if n==1:
            return 0
        while s<=e:
            mid = s + ( e - s )//2
            if mid > 0 and mid < n-1: 
                #here we are not taking the end elements..that is to be handled in else part ,they need seperate attention
                if arr[mid-1]<arr[mid]>arr[mid+1]:
                    return mid
                elif arr[mid]<arr[mid+1]:
                    s=mid+1
                else:
                    e=mid-1
            elif mid == 0 :
                # now handling the ends or edges
                if arr[0]>arr[1]:
                    return 0
                else:
                    return 1
            elif mid == n-1:
                if arr[mid]>arr[n-2]:
                    return mid
                else:
                    return n-2 