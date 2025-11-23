class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n=len(nums)
        ans1,ans2=0,0
        s=0
        nums.sort()
        for i in range(n):
            s+=nums[i]
        if s%3==0:
            return s
        elif s%3==1:
            for i in range(n):
                if nums[i]%3==1:
                    ans1=s-nums[i]
                    break
            c=0
            for i in range(n):
                if nums[i]%3==2:
                    c+=1
                    s=s-nums[i]
                    if c==2:
                        ans2=s
                        break
            return max(ans1,ans2)

        else:
            for i in range(n):
                if nums[i]%3==2:
                    ans1=s-nums[i]
                    break
            c=0
            for i in range(n):
                if nums[i]%3==1:
                    c+=1
                    s=s-nums[i]
                    if c==2:
                        ans2=s
                        break
            return max(ans1,ans2)
        return 0

        