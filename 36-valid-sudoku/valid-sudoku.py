class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=[[False]*10 for i in range(9)]
        col=[[False]*10 for i in range(9)]
        boxes=[[False]*10 for i in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c]!=".":
                    num = int(board[r][c])
                    box = (r//3)*3 + (c//3)
                    if row[r][num]==True:
                        return False
                    if col[c][num]==True:
                        return False
                    if boxes[box][num]==True:
                        return False
                    row[r][num] =True
                    col[c][num] = True
                    boxes[box][num] = True
        return True

    