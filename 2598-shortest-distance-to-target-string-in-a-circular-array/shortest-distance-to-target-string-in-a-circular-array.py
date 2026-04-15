class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        ans=float('inf')
        ans_i=0
        for i in range(len(words)):
            if words[i]==target:
                ans_i=i
                x=min(abs(startIndex-ans_i),len(words)-abs(startIndex-(ans_i)))
                ans=min(ans,x)
        if ans==float('inf'):
            return -1
        return ans        

        