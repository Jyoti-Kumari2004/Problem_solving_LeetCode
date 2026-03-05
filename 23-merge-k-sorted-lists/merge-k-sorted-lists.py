# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q=[]
        for i in range(len(lists)):
            if lists[i]==None:
                continue
            heapq.heappush(q,[lists[i].val,i,lists[i]])
        head=ListNode(0)
        temp=head
        while q:
            val,ind,node=heapq.heappop(q)
            temp.next=node
            temp=temp.next
            if node.next:
                heapq.heappush(q,[node.next.val,ind,node.next])
        return head.next

