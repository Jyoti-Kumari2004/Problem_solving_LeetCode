# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak=self.peakofMountain(mountainArr)
        a=self.BSasce(mountainArr,target,0,peak-1)
        b=self.BSdesc(mountainArr,target,peak,mountainArr.length()-1)
        if a==-1 and b==-1:
            return -1
        elif a==-1 or b==-1:
            return max(a,b)
        else:
            return min(a,b)

        
    def peakofMountain(self,mountainArr):
        n=mountainArr.length()
        s=0
        e=n-1
        if n==1:
            return 0
        while s<=e:
            mid = s + ( e - s )//2
            if mid > 0 and mid < n-1: 
                #here we are not taking the end elements..that is to be handled in else part ,they need seperate attention
                if mountainArr.get(mid-1)< mountainArr.get(mid)> mountainArr.get(mid+1):
                    return mid
                elif mountainArr.get(mid)<mountainArr.get(mid+1):
                    s=mid+1
                else:
                    e=mid-1
            elif mid == 0 :
                # now handling the ends or edges
                if mountainArr.get(0)>mountainArr.get(1):
                    return 0
                else:
                    return 1
            elif mid == n-1:
                if mountainArr.get(mid)>mountainArr.get(n-2):
                    return mid
                else:
                    return n-2
    def BSasce(self,mountainArr,key,s,e):
        while s<=e:
            mid=s+(e-s)//2
            val=mountainArr.get(mid)
            if val==key:
                return mid
            elif val>key:
                e=mid-1
            else:
                s=mid+1
        return -1
    def BSdesc(self,mountainArr,key,s,e):
        while s<=e:
            mid=s+(e-s)//2
            val=mountainArr.get(mid)
            if val==key:
                return mid
            elif val<key:
                e=mid-1
            else:
                s=mid+1
        return -1
    