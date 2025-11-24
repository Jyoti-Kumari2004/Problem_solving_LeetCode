class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        # ans=[]
        # sum=0
        # for i in range(len(nums)):
        #     sum+=(2**i)
        #     if sum%5==0:
        #         ans.append(True)
        #     else:
        #         ans.append(False)
        #     print(sum)
            
        # return ans

        ans=[]
        n=0
        for ch in nums:
            n=(n*2+ch)%5
            ans.append(n==0)
        return ans