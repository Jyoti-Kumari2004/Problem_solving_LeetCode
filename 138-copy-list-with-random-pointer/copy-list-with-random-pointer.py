"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d=defaultdict(int)
        temp=head
        while temp!=None:
            new_node=Node(temp.val)
            d[temp]=new_node
            temp=temp.next
        print(d)
        temp=head
        tail=Node(-1)
        h=tail
        while temp!=None:
            node=d[temp]
            if temp.next!=None:
                node.next=d[temp.next]
            else:
                node.next=None
            if temp.random!=None:
                node.random=d[temp.random]
            else:
                node.random=None
            tail.next=node
            tail=tail.next
            temp=temp.next
        tail.next=None
        return h.next
            

