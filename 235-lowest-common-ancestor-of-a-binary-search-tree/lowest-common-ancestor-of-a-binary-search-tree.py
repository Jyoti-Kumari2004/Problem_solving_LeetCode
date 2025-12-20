# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        if p.val<root.val and q.val<root.val:
            ls=self.lowestCommonAncestor(root.left,p,q)
            if root!=None:
                return ls
        if  p.val>root.val and q.val>root.val:
            rs=self.lowestCommonAncestor(root.right,p,q)
            if root!=None:
                return rs
        return root

                   
        
        



        