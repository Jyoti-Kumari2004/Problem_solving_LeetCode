# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        ans=[]
        q.append(root)
        while q:
            ls=[]
            for i in range(len(q)):
                node=q.popleft()
                ls.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(self.avg(ls))
        return ans
    def avg(self,arr):
        return sum(arr)/len(arr)
        