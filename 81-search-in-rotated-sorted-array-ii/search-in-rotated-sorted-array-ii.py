class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums)==1: 
            return target==nums[0] 
        if len(nums)==2: 
            return nums[0]==target or nums[1]==target
        s=0
        e=len(nums)-1
        while s<=e:
            mid=s+(e-s)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[e]==nums[s]:
                s+=1
                e-=1
            elif nums[s]<=nums[mid]:
                if nums[s]<=target<nums[mid]:
                    e=mid-1
                else:
                    s=mid+1
            else:
                if nums[mid]<target<=nums[e]:
                    s=mid+1
                else:
                    e=mid-1
        return False
