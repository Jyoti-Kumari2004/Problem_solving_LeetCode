class Solution:
    def jump(self, nums: List[int]) -> int:
        end=0
        jump=0
        door=0
        for i in range(len(nums)-1):
            door=max(door,nums[i]+i)
            if i==end:
                jump+=1
                end=door
        return jump

        
        