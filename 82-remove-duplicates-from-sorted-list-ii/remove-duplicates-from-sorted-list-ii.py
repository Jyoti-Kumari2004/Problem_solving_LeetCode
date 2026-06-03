# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail=ListNode(-1)
        new_head=tail
        temp=head
        while temp!=None:
            new=temp
            k=0
            while new and new.val==temp.val:
                k+=1
                new=new.next
            if k==1:
                tail.next=temp
                tail=tail.next
            temp=new
        tail.next=None
        return new_head.next

            
        