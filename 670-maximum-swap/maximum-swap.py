class Solution:
    def maximumSwap(self, num: int) -> int:
        #effiecient method
        s=str(num)
        li=list(s)
        li=list(map(int,li))
        rightMax=[0]*len(li)
        rightMax[-1]=len(li)-1
        for i in range(len(li)-2,-1,-1):
            if li[rightMax[i+1]]<li[i]:
                rightMax[i]=i
            else:
                rightMax[i]=rightMax[i+1]
        for i in range(len(li)):
            if li[i]!=li[rightMax[i]]:
                li[i],li[rightMax[i]]=li[rightMax[i]],li[i]
                ss=list(map(str,li))
                return int("".join(ss))
        return int(num)















        #trying out all possibilites....that is a bit lenthy process and inefficent
    #     s=str(num)
    #     res=s
    #     for i in range(len(s)):
    #         maxi=max(s[i:])
    #         for j in range(i,len(s)):
    #             if s[j]==maxi and s[j]>s[i]:
    #                 s=self.swap(s,i,j)
    #                 res=max(s,res)
    #                 s=self.swap(s,i,j)
    #     return int(res)
    # def swap(self,s,i,j):
    #     v=list(s)
    #     v[i],v[j]=v[j],v[i]
    #     return "".join(v)


            