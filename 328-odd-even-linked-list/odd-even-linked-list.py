# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None or head.next.next==None:
            return head
        else:
            return self.solve(head)
        
    def solve(self,head):
        od=head
        ev=head.next
        ev_head=ev
        while ev!=None and ev.next!=None:
            od.next=od.next.next
            ev.next=ev.next.next

            od=od.next
            ev=ev.next
        od.next=ev_head
        return head
        
        

        
        