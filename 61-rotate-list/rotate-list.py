# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None or k==0:
            return head
        
        n=0
        temp=head
        while temp!=None:
            temp=temp.next
            n+=1

        s=head
        f=head
        k=k%n
        if k==0:
            return head
        while k>0 and f.next!=None:
            f=f.next
            k-=1
        while s and f.next:
            s=s.next
            f=f.next

        nh=s.next
        s.next=None
        f.next=head
        return nh
