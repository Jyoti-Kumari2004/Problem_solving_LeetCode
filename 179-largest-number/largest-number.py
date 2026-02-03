class Solution:
    def largestNumber(self, numi: List[int]) -> str:
        if len(numi)==1:
            return str(numi[0])
        nums=[]
        count=0
        for i in range(len(numi)):
            if numi[i]==0:
                count+=1
            else:
                nums.append(numi[i])
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if int(str(nums[i])+str(nums[j]))<int(str(nums[j])+str(nums[i])):
                    print("ji")
                    print(str(nums[i])+str(nums[j]))
                    print(str(nums[j])+str(nums[i]))
                    nums[i],nums[j]=nums[j],nums[i]
        if not nums:
            return '0'
        return ''.join(map(str,nums))+("0"*count)
        