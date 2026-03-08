class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d=defaultdict(int)
        for num in arr:
            d[num]+=1
        n=set(d.values())
        return len(n)==len(d)

        