from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, arr: List[int], k: int) -> int:
        i=0
        j=0
        res=0
        sum=0
        hash=defaultdict(int)
        while j<len(arr):
            hash[arr[j]]+=1
            while hash[arr[j]]>1:
                hash[arr[i]]-=1
                sum -= arr[i]
                i += 1
            sum+=arr[j]
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                res=max(res,sum)
                sum-=arr[i]
                hash[arr[i]]-=1
                i+=1
                j+=1
        print(hash)
        return res


        