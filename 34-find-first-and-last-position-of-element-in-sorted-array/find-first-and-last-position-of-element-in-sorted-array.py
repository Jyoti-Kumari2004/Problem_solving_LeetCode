class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        f=self.first(nums,target)
        e=self.last(nums,target)
        return [f,e]
    def first(self,nums,target):
        s=0
        e=len(nums)-1
        mid=0
        while(s<=e):
            mid=s+(e-s)//2
            if target>nums[mid]:
                s=mid+1
            elif target<nums[mid]:
                e=mid-1
            else:
                if  mid == 0 or nums[mid-1]!=nums[mid]:
                    return mid
                else:
                    e=mid-1
        return -1
    def last(self,nums,target):
        s=0
        e=len(nums)-1
        mid=0
        while(s<=e):
            mid=s+(e-s)//2
            if target<nums[mid]:
                e=mid-1
            elif target>nums[mid]:
                s=mid+1
            else:
                if  mid == len(nums)-1 or nums[mid+1]!=nums[mid]:
                    return mid
                else:
                    s=mid+1
        return -1
        

    
        