# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverse(self,arr):
        return arr[::-1]
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        count=1
        if root==None:
            return []
        ans=[]
        q=deque()
        q.append(root)
        while (len(q)):
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.val) 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if count==0:
                ans.append(self.reverse(level))
                count=1
            else:
                ans.append(level)
                count=0

        return ans