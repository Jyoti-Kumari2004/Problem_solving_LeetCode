# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        return self.mergeSort(head)
    
    def mergeSort(self,head):
        if not head or not head.next:
            return head
        slow=head
        fast=head
        prev=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        left=self.mergeSort(head)
        right=self.mergeSort(slow)
        return self.merge(left,right)
        


    def merge(self,head1,head2):
        temp1=head1
        temp2=head2
        tail=ListNode(-1)
        dummy=tail
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                tail.next=temp1
                temp1=temp1.next
                tail=tail.next
            elif temp2.val<temp1.val:
                tail.next=temp2
                temp2=temp2.next
                tail=tail.next
        if temp1:
            tail.next=temp1
        if temp2:
            tail.next=temp2  
        return dummy.next


        