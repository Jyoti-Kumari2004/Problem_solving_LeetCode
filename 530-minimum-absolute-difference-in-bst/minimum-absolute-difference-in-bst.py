# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        prev=None
        ans=[float('inf')]
        self.solve(root,ans,prev)
        return ans[0]

    def solve(self,root,ans,prev):
        if root==None:
            return prev 
        prev=self.solve(root.left,ans,prev)
        if prev is not None:
            ans[0] = min(ans[0], abs(root.val - prev))
        prev=root.val
        prev = self.solve(root.right, ans, prev)
        return prev

        