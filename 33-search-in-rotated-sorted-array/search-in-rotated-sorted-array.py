class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l=0
        h=len(arr)-1
        mid=0
        while l<=h:
            mid=l+((h-l)//2)
            if arr[mid]==target:
                return mid
            elif arr[l]<=arr[mid]:
                if target>=arr[l] and target<arr[mid]:
                    h=mid-1
                else:
                    l=mid+1
            else:
                if target>arr[mid] and target<=arr[h]:
                    l=mid+1
                else:
                    h=mid-1

            
        return -1


        