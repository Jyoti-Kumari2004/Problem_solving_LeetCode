# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        summ=0
        return self.helper(root,summ,targetSum)
    def helper(self,root,summ,targetSum):
        if root==None:
            return False
        summ+=root.val
        if summ==targetSum and root.left==None and root.right==None:
            return True
        return self.helper(root.left,summ,targetSum) or self.helper(root.right,summ,targetSum)
        