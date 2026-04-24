class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ele1=0
        ele2=0
        c1=0
        c2=0
        for i in range(len(nums)):
            if c1==0 and ele2!=nums[i]:
                ele1=nums[i]
                c1=1
            elif c2==0 and ele1!=nums[i]:
                ele2=nums[i]
                c2=1
            elif ele1==nums[i]:
                c1+=1
            elif ele2==nums[i]:
                c2+=1
            else:
                c1-=1
                c2-=1
        c1,c2=0,0
        if ele1==ele2:
            return [ele1]
        for i in range(len(nums)):
            if nums[i]==ele1:
                c1+=1
            if nums[i]==ele2:
                c2+=1
        if c1>len(nums)//3 and c2>len(nums)//3:
            return [ele1,ele2]
        elif c1>len(nums)//3:
            return [ele1]
        elif c2>len(nums)//3:
            return [ele2]
        else:
            return []
        