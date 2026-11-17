# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        t1=list1
        t2=list2
        tailh=ListNode(-1)
        tail=tailh
        while t1 and t2:
            if t1.val<=t2.val:
                tail.next=t1
                t1=t1.next
            else:
                tail.next=t2
                t2=t2.next
            tail=tail.next
        if t1:
            tail.next=t1
            t1=t1.next
            tail=tail.next
        if t2:
            tail.next=t2
            t2=t2.next
            tail=tail.next
        return tailh.next
        