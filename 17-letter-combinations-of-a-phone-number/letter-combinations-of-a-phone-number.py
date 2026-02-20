class Solution:
    def __init__(self):
        self.map = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}

    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        self.solve(digits,0,res,[]) 
        return res
        
    def solve(self,s,ind,res,path):
        if ind==len(s):
            res.append("".join(path.copy()))
            return
        for i in range(0,len(self.map[s[ind]])): 
            path.append(self.map[s[ind]][i])
            self.solve(s,ind+1,res,path)
            path.pop()


        