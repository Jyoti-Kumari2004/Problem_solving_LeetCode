class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        for i in range(len(spells)):
            ind=self.solve(spells[i],success,potions)
            ans.append(len(potions)-ind)
            
        return ans
    def solve(self,num,pro,arr):
        s=0
        e=len(arr)-1
        ans=len(arr)
        while s<=e:
            mid=s+(e-s)//2
            if num*arr[mid]>=pro:
                ans=mid
                e=mid-1
            else:
                s=mid+1
        return ans
