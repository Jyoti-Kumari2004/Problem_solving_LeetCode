class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        bt=[i for i in range(n)]
        t=[1]*n
        ans_i=0
        ans=0
        for i in range(n):
            maxi=0
            for j in range(i):
                if nums[i]%nums[j]==0 or nums[j]%nums[i]==0 :
                    if maxi<1+t[j]:
                        maxi=max(maxi,1+t[j])
                        bt[i]=j
            t[i]=maxi
            if ans<maxi:
                ans=maxi
                ans_i=i
        sol=[]
        sol.append(nums[ans_i])
        while bt[ans_i]!=ans_i:
            ans_i=bt[ans_i]
            sol.append(nums[ans_i])
        return sol[::-1]

        