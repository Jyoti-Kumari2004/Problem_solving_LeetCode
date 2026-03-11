class Solution:
    def bitwiseComplement(self, n: int) -> int:
        s=""
        ns=bin(n)[2:]
        for ch in ns:
            if ch=="1":
                s+="0"
            elif ch=="0":
                s+="1"
        return int(s,2)
        