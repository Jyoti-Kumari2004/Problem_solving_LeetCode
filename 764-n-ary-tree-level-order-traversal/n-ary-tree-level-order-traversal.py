"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root==None:
            return []
        q=deque()
        res=[]
        q.append(root)
        while q:
            path=[]
            for i in range(len(q)):
                node=q.popleft()
                path.append(node.val)
                for child_node in node.children:
                    if child_node!=None:
                        q.append(child_node)
            res.append(path)
        return res
                
        