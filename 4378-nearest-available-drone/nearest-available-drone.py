class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        i=0
        ans=-1
        ansv=float('inf')
        for x,y,rg in drones:
            curr=abs(target[0]-x)+abs(target[1]-y)
            print(curr,i)
            if curr<=rg:
                if curr<ansv:
                    ans=i
                    ansv=curr
                if curr==ansv:
                    ans=min(ans,i)
                    ansv=curr
            i+=1
        return ans
        