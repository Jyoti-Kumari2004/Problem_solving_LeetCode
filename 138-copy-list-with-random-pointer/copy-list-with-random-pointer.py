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
        if not head:
            return None
        temp=head
        while temp!=None:
            new_node=Node(temp.val)
            next=temp.next
            temp.next=new_node
            new_node.next=next
            temp=temp.next.next
        temp=head
        while temp:
            if temp.random:
                temp.next.random=temp.random.next
            else:
                temp.next.random=None
            temp=temp.next.next
        curr=head.next
        nh=curr
        while curr.next!=None:
            curr.next=curr.next.next
            curr=curr.next
        return nh

















        # this is taking more time , not very efficient because this uses hashmap
        # d=defaultdict(int)
        # temp=head
        # while temp!=None:
        #     new_node=Node(temp.val)
        #     d[temp]=new_node
        #     temp=temp.next
        # print(d)
        # temp=head
        # tail=Node(-1)
        # h=tail
        # while temp!=None:
        #     node=d[temp]
        #     if temp.next!=None:
        #         node.next=d[temp.next]
        #     else:
        #         node.next=None
        #     if temp.random!=None:
        #         node.random=d[temp.random]
        #     else:
        #         node.random=None
        #     tail.next=node
        #     tail=tail.next
        #     temp=temp.next
        # tail.next=None
        # return h.next
            

