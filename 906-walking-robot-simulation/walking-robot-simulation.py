class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob=set()
        for lis in obstacles:
            ob.add(tuple(lis))
        n,m=0,0
        curr_dir="N"
        curr_i,curr_j=0,1
        ans=0
        for i in range(len(commands)):
            if commands[i]==-1:
                curr_i,curr_j=curr_j,-curr_i
            elif commands[i]==-2:
                curr_i,curr_j=-curr_j,curr_i,
            else:
                x,y=curr_i,curr_j
                for _ in range(commands[i]):
                    if (n+x,m+y) in ob:
                        break
                    n+=x
                    m+=y
                    ans=max(ans,n*n+m*m)
        return ans
                    

        