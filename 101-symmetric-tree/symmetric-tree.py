# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Mirror(l,r):
            if not l and not r:
                return True
            if l and not r:
                return False
            if not l and r:
                return False
            if l.val!=r.val:
                return False
            left=l
            right=r
            return Mirror(left.left,right.right) and Mirror(left.right,right.left)
        return Mirror(root.left,root.right)
                
        
            
        



