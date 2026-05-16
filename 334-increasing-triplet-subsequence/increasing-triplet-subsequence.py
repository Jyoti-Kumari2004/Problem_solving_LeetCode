class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        temp=[]
        temp.append(nums[0])
        for i in range(len(nums)):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                ind=self.lowerbound(nums[i],temp)
                temp[ind]=nums[i]
        if len(temp)>=3:
            return True
        return False
    def lowerbound(self,num,arr):
        s,e=0,len(arr)-1
        while s<e:
            mid=s+(e-s)//2
            if arr[mid]<num:
                s=mid+1
            else:
                e=mid
        return s

        