class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left=0
        for ch in moves:
            if ch=="L" or ch=="_":
                left+=1
            else:
                left-=1
        right=0
        for ch in moves:
            if ch=="R" or ch=="_":
                right+=1
            else:
                right-=1
        return max(abs(left),abs(right))
        