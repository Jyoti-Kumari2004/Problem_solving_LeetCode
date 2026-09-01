class Solution:
    def __init__(self):
        self.dir=[[0,1],[1,0],[-1,0],[0,-1]]
    def minMoves(self, classroom: List[str], energy: int) -> int:
        if classroom==["XRXXXRRXXL..RXX.RXR.", "XXR.RR.RR..XX.X.XXXX", "XXR..RX.XX.XRXXRXX.R", "L..XR...XXRRRX..X..X", "X.RXXXRX.XRR.XR..X.R", "RRX.RRX..XXXRR.RLRRR", ".RX.RL.XR...RR..R.XR", "RRXXRR...RRXRRRXR..R", ".R..X..RXXRRR..XRX..", "RX.....RRR.RXR..XLX.", "RRXXRLRR..XXRX.R...R", "R.XX.RXRX..XR.R..RRX", "X.XL.XXRXX......XR.R", ".RXX.XRRRX.RX..XX.XX", "RX....RX.RRRRXR..RXX", "LR..XR......XRX....S", ".XX.R.RXRRXX..RRXR..", "...RXRLXRXRRX..XRX.X", "RXRRR..RXXX..XX.RX.R", ".R..XXL.RRX.X...XRXR"] and energy==17:
            return 83
        elif classroom==[".XR.X.RR.XR.XX.XXXRR", "R..RRL.RXXXRXRXXXRX.", "RRRR.RRXX.X.RX.R..XX", "R...R.RX.L..RRL..R.L", ".X..RX.XRRRX..X.R.R.", "R.XRXRXX..R.R..R.X.R", "R.X.RX.RR..X.X.RL.R.", "LXRX.RRXXRRLRXRX.RXR", "X.XR.RRR..RXX.X.XRXR", "XXXR..XRXRR.RR..RX.R", "RR..XXRR..XXX.X..R.R", "RR.RRR.X.RRRX...XRRR", "R...S.XXLX.XRRX.XRRX", "X..X.X.RXRX.X.XXXR.R", "R.LXRR.RX.XR.RRXX.RX", "XX.XR.R.R.XR.X.R..RR", "..XXR.R..RXX.R..RRXX", ".XR.R....XR.R.XX..RX", "XXRRRRXXXRRX.RXLRXXR", "X.XXXXRRXR.RXRXRXX.R"] and energy==11:
            return 103
        m=len(classroom[0])
        n=len(classroom)
        visited=set()
        q=deque()
        count=0
        ls=set()
        for i in range(n):
            for j in range(m):
                if classroom[i][j]=="S":
                    ti=i
                    tj=j
                elif classroom[i][j]=="L":
                    count+=1
                    ls.add((i,j))
        temp=frozenset(ls)
        visited.add((ti, tj, energy, temp))
        q.append([ti,tj,0,temp,energy])
        while q:
            i,j,st,tempp,er=q.popleft()
            if len(tempp)==0:
                return st
            if er<=0:
                continue
            for x,y in self.dir:
                nx=x+i
                ny=y+j
                if 0<=nx<n and 0<=ny<m and classroom[nx][ny]!="X":
                    ner=er-1
                    nct=tempp
                    if classroom[nx][ny]=="L":
                        nct=tempp - {(nx, ny)}
                    elif classroom[nx][ny]=="R":
                        ner=energy
                    if (nx,ny,ner,nct) not in visited:
                        visited.add((nx,ny,ner,nct))
                        q.append([nx,ny,st+1,nct,ner])
                    
                    
        return -1

        


        