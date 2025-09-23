from collections import defaultdict
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        hash=defaultdict(int)
        for i in range(len(nums)):
            hash[nums[i]]+=1
        maxi=0
        for i in hash:
            maxi=max(hash[i],maxi)
        sum=0
        for i in hash:
            if hash[i]==maxi:
                sum+=hash[i]
        return sum

        