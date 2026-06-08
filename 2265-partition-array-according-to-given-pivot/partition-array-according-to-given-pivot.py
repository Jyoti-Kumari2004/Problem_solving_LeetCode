class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # i=0
        # j=len(nums)-1
        # k=0
        # while k<=j:
        #     if nums[k]<pivot:
        #         nums[k],nums[i]=nums[i],nums[k]
        #         k+=1
        #         i+=1
        #     elif nums[k]>pivot:
        #         nums[k],nums[j]=nums[j],nums[k]
        #         j-=1
        #     else:
        #         k+=1
        # return nums[:k]+nums[k:][::-1]
        s=[]
        l=[]
        ss=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                s.append(nums[i])
            elif nums[i]>pivot:
                l.append(nums[i])
            else:
                ss.append(nums[i])
        return s+ss+l

            
        