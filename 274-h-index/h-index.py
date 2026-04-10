class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        n=len(citations)
        if n==1:
            if citations[0]>=1:
                return 1
            return 0
        for i in range(n):
            if citations[i]<i+1:
                return i
        return n
        