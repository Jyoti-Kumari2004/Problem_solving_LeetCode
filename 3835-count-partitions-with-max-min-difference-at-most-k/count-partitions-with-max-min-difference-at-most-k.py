from collections import deque
class Solution:
    def countPartitions(self, nums, k)->int:
        
        
        n = len(nums)
        mod = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        pref = [0] * (n + 1)
        pref[0] = 1
        
        maxD, minD = deque(), deque()
        l = 0
        
        for r in range(n):
            while maxD and maxD[-1] < nums[r]:
                maxD.pop()
            maxD.append(nums[r])
            
            while minD and minD[-1] > nums[r]:
                minD.pop()
            minD.append(nums[r])
            
            while maxD[0] - minD[0] > k:
                if nums[l] == maxD[0]:
                    maxD.popleft()
                if nums[l] == minD[0]:
                    minD.popleft()
                l += 1
            
            t = pref[r] - (pref[l - 1] if l > 0 else 0)
            dp[r + 1] = t % mod
            
            pref[r + 1] = (pref[r] + dp[r + 1]) % mod
        
        return dp[n]
