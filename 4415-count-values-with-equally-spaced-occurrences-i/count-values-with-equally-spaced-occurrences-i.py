class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d=defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)
        c=0
        for key,value in d.items():
            if len(value)==3 and value[1]-value[0]==value[2]-value[1]:
                c+=1
        return c