class Solution:
    #solving this using greedy, in O(n) time and O(1) space complexity
    def candy(self, ratings: List[int]) -> int:
        s,i=1,1
        while i<len(ratings):
            if ratings[i]==ratings[i-1]:
                s+=1
                i+=1
                continue
            peak=1
            while i<len(ratings) and ratings[i]>ratings[i-1]:
                peak+=1
                s+=peak
                i+=1
            down=1
            while i<len(ratings) and ratings[i]<ratings[i-1]:
                s+=down
                down+=1
                i+=1
            if down>peak:
                s+=down-peak
        return s
            






        
















    #this is also takein O(n) time and O(n) space, i need to remove the space
    # def candy(self, ratings: List[int]) -> int:
    #     pref=[0]*len(ratings)
    #     suff=[0]*len(ratings)
    #     pref[0]=1
    #     for i in range(1,len(ratings)):
    #         if ratings[i]>ratings[i-1]:
    #             pref[i]=pref[i-1]+1
    #         else:
    #             pref[i]=1
    #     suff=1
    #     summ=max(1,pref[-1])
    #     for i in range(len(ratings)-2,-1,-1):
    #         if ratings[i]>ratings[i+1]:
    #             suff=suff+1
    #         else:
    #             suff=1
    #         summ+=max(pref[i],suff)
    #     print(suff)
    #     return summ
        



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
        
        