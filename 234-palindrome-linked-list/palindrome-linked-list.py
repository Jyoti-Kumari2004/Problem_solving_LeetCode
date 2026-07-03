# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return True
        slow=head
        fast=head
        prev=head
        c=0
        while fast and fast.next:
            c+=1
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=self.reverse(slow)
        a=head
        b=prev.next
        while c and a and b:
            c-=1
            if a.val!=b.val:
                return False
            a=a.next
            b=b.next
        return True
       
        
    def reverse(self,head):
        next=curr=head
        prev=None
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
