# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.t={}
    def rob(self, root: TreeNode | None) -> int:
        return self.solve(root,0)
    def solve(self,root,take):
        if root==None:
            return 0
        if (root,take) in self.t:
            return self.t[(root,take)]
        if take==1:
            l=self.solve(root.left,0)
            r=self.solve(root.right,0)
            ans= l+r
        else:
            take_root=root.val+self.solve(root.left,1)+self.solve(root.right,1)
            skip_root=self.solve(root.left,0)+self.solve(root.right,0)
            ans= max(take_root,skip_root)
        self.t[(root,take)]=ans
        return ans
        
