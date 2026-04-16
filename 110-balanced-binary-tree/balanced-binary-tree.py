# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.solve(root)==-1:
            return False
        else:
            return True


    def solve(self,root):
        if root==None:
            return 0
        ls=self.solve(root.left)
        rs=self.solve(root.right)
        if ls==-1 or rs==-1:
            return -1
        if abs(ls-rs)>1:
            flag=True
            return -1
        return 1+max(ls,rs)
        
        