class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d=defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        c=0
        for key,value in d.items():
            if len(value)>=3:
                dif=value[1]-value[0]
                flag=True
                for i in range(1,len(value)):
                    if value[i]-value[i-1]!=dif:
                        flag=False
                        break
                if flag==True:
                    c+=1
        return c