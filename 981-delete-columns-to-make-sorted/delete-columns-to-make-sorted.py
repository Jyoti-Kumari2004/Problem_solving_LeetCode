class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        no_of_col=len(strs[0])
        lis=[[]for i in range(no_of_col)]
        for j in range(no_of_col):
            for i in range(len(strs)):
                lis[j].append(strs[i][j])
        print(lis)
        count=0
        for l in range(len(lis)):
            if lis[l]!=sorted(lis[l]):
                count+=1
        return count
                
