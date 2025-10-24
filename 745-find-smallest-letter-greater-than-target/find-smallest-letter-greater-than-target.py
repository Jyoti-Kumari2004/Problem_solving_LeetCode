class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s=0
        e=len(letters)-1
        mid=0
        ans=letters[0]
        while s<=e:
            mid=s+(e-s)//2
            if letters[mid]>target:
                ans=letters[mid]
                e=mid-1
            else:
                s=mid+1
        return ans
