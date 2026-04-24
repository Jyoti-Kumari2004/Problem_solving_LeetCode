"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q=deque()
        d={}
        q.append(node)
        root=Node(node.val)
        d[node]=root
        while q:
            nodee=q.popleft()
            for u in nodee.neighbors:
                if u not in d:
                    new_node=Node(u.val)
                    d[u]=new_node
                    q.append(u)
                
                d[nodee].neighbors.append(d[u])
            
        return root
        