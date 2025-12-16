# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        summ=0
        count=0
        return self.F1(root,targetSum,summ,count)
    def F1(self,root,targetSum,summ,count):
        if root==None:
            return 0
        return self.F1(root.left,targetSum,summ,count)+self.F1(root.right,targetSum,summ,count)+self.F2(root,targetSum,summ,count)
    def F2(self,root,targetSum,summ,count):
        if root==None:
            return 0
        summ+=root.val
        if targetSum==summ:
            count=1
        else:
            count=0
        ls=self.F2(root.left,targetSum,summ,count)
        rs=self.F2(root.right,targetSum,summ,count)
        return count+ls+rs
