class Solution:
    def findNumberOfLIS(self, arr: List[int]) -> int:
        n=len(arr)
        t=[1]*(n)
        cnt=[1]*(n)
        ans=1
        for i in range(1,n):
            maxi=1
            c=0
            for j in range(i):
                if arr[i]>arr[j] and t[j]+1>maxi:
                    maxi=max(1+t[j],maxi)
                    cnt[i]=cnt[j]
                elif arr[i]>arr[j] and t[j]+1==maxi:
                    cnt[i]+=cnt[j]
                    
            t[i]=maxi
            ans=max(ans,maxi)
        nos=0
        for i in range(len(t)):
            if t[i]==ans:
                nos+=cnt[i]
        
        return nos