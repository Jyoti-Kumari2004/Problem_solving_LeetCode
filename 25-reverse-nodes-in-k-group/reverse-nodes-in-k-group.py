# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        nh=head
        tail=ListNode(-1)
        th=tail
        flag=False
        while temp!=None:
            nk=k
            prev=temp
            while nk and temp!=None:
                nk-=1
                prev=temp
                temp=temp.next
            if nk==0:
                prev.next=None
                tail.next=self.reverse(nh)
                tail=nh
                nh=temp
            else:
                tail.next=nh
                break
        return th.next
            


    def reverse(self,head):
        if head==None:
            return None
        curr=head
        next=head
        prev=None
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
        