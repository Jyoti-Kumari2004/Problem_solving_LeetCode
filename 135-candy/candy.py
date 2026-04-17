class Solution:
    def candy(self, ratings: List[int]) -> int:
        pref=[0]*len(ratings)
        suff=[0]*len(ratings)
        pref[0]=1
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                pref[i]=pref[i-1]+1
            else:
                pref[i]=1
        suff=1
        summ=max(1,pref[-1])
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                suff=suff+1
            else:
                suff=1
            summ+=max(pref[i],suff)
        print(suff)
        return summ
        


    #using first naive approach , this is O(4n) time and O(3n) space
    # def candy(self, ratings: List[int]) -> int:
    #     pref=[0]*len(ratings)
    #     suff=[0]*len(ratings)
    #     pref[0]=1
    #     for i in range(1,len(ratings)):
    #         if ratings[i]>ratings[i-1]:
    #             pref[i]=pref[i-1]+1
    #         else:
    #             pref[i]=1
    #     print(pref)
    #     suff[-1]=1
    #     for i in range(len(ratings)-2,-1,-1):
    #         if ratings[i]>ratings[i+1]:
    #             suff[i]=suff[i+1]+1
    #         else:
    #             suff[i]=1
    #     print(suff)
    #     res=[]
    #     for m,n in zip(pref,suff):
    #         res.append(max(m,n))
    #     return sum(res)
        