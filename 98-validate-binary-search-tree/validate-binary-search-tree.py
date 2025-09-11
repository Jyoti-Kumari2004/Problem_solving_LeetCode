# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(root,minv=float('-inf'),maxv=float('inf')):
            if root==None:
                return True
            if root.val<minv or root.val>maxv:
                return False
            return validity(root.right,root.val+1,maxv) and validity(root.left,minv,root.val-1)
        return validity(root)
        
        