class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dir={"U":[-1,0],"D":[1,0],"R":[0,1],"L":[0,-1]}
        i=0
        j=0
        for m in moves:
            x,y=dir[m]
            i+=x
            j+=y
        return 0==i and 0==j

        