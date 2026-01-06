# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res=[]
        q=deque() 
        q.append(root)
        while q:
            summ=0
            for i in range(len(q)):
                node=q.popleft()
                summ+=node.val 
                if node.right is not None:
                    q.append(node.right)
                if node.left is not None:
                    q.append(node.left)
            res.append(summ)
        return res.index(max(res))+1
