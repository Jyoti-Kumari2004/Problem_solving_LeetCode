class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        left=[-1]*len(colors)
        for i in range(1,len(colors)):
            if colors[0]!=colors[i]:
                left[i]=i
            else:
                left[i]=-1
        right=[-1]*len(colors)
        n=len(colors)
        for j in range(len(colors)-2,-1,-1):
            if colors[-1]!=colors[j]:
                right[j]=n-j-1
            else:
                right[j]=-1
        ans=0
        i=0
        j=0
        while i<len(left) and j<len(right):
            if left[i]!=-1:
                ans=max(ans,left[i])
            if right[j]!=-1:
                ans=max(ans,right[j])
            i+=1
            j+=1
        print(left,right)
        return ans


        