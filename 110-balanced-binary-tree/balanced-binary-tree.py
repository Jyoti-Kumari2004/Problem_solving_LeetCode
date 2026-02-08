# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.Boo=True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.solve(root)
        if self.Boo==False:
            return False
        return True
    def solve(self,root):
        if root==None:
            return 0
        ls=self.solve(root.left)
        rs=self.solve(root.right)
        if abs(ls-rs)>1:
            self.Boo=False
        return max(ls,rs)+1