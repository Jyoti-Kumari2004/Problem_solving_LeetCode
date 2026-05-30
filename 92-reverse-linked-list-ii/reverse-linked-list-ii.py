# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        pos=1
        prevl=None
        while pos<left:
            prevl=curr
            curr=curr.next
            pos+=1
        if curr==None:
            return head
        leftp=curr
        beforel=prevl
        while curr.next!=None and pos<right:
            curr=curr.next
            pos+=1

        rightp=curr
        afterright=curr.next
        x=self.reverse(leftp,rightp)
        if beforel:
            beforel.next=x
        else:
            head=x
        leftp.next=afterright
        return head



    def reverse(self,head,end):
        curr=head
        prev=None
        next=head
        stop=end.next
        while curr!=stop:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev




        