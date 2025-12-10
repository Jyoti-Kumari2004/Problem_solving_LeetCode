class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        for i in range(1,len(complexity)):
            if complexity[0]>=complexity[i]:
                return 0
        fact=1
        for j in range(1,len(complexity)):
            fact*=j
        return fact%1000000007
