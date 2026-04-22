class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        grps=[]
        count=0
        curr=[]
        for word in words:
            count+=len(word)
            count+=1
            if count-1>maxWidth:
                grps.append(curr)
                curr=[]
                count=0
                curr.append(word)
                count+=len(word)
                count+=1
            else:
                curr.append(word)
        grps.append(curr)
        #now we have group
        fin=[]
        lc=0
        for j in range(len(grps)):
            lc=0
            curr=""
            for word in grps[j]:
                lc+=len(word)
            total_spaces=maxWidth-lc
            necess=len(grps[j])-1
            if necess==0:
                curr+=grps[j][0]
                curr+=" "*(maxWidth-len(curr))
                fin.append(curr)
                continue
            extra_space=total_spaces//necess
            extra=total_spaces%necess
            if j==len(grps)-1:
                for i in range(len(grps[j])):
                    curr+=grps[j][i]
                    if i!=len(grps[j])-1:
                        curr+=" "
                use=maxWidth-len(curr)
                print(use)
                curr+=" "*use
            else:
                for i in range(len(grps[j])):
                    curr+=grps[j][i]
                    if i!=len(grps[j])-1:
                        curr+=" "*extra_space
                        if extra>0:
                            curr+=" "
                            extra-=1
                
                
            fin.append(curr)

        return fin









        