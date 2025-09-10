# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxi=float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def loop(root):
            if root==None:
                return 0
            ls=max(0,loop(root.left))
            rs=max(0,loop(root.right))
            sum=ls+rs+root.val
            self.maxi=max(sum,self.maxi)
            return max(ls,rs)+root.val
        loop(root)
        return self.maxi
        
















        # if root==None:
        #     return 0
        # else:
        #     ls=self.maxPathSum(root.left)
        #     rs=self.maxPathSum(root.right)
        #     if ls and rs:
        #         if ls>0 and rs>0 and root.val>0:
        #             return ls+rs+root.val
        #         elif ls<0 and rs<0 and root.val>0:
        #             return root.val
        #         elif root.val<0:
        #             return max(ls,rs)
        #         elif ls<0 and rs>0 and root.val>0:
        #             return root.val+rs
        #         elif ls>0 and root.val>0 and rs<0:
        #             return root.val+ls
        #         elif ls==rs==0:
        #             return root.val
        #         else:
        #             return 0
    

        
                

            