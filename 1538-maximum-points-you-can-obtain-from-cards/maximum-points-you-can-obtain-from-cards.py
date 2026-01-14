class Solution:
    def maxScore(self, arr: List[int], k: int) -> int:
        summ=0
        for i in range(k):
            summ+=arr[i]
        print(i,summ)
        m=summ
        j=len(arr)-1
        while k>0:
            summ-=arr[i]
            summ+=arr[j]
            m=max(summ,m)
            k-=1
            i-=1
            j-=1
        return m






