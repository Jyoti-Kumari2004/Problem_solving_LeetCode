# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        temp=head
        tail=ListNode(-1)
        st=ListNode(-1)
        th=tail
        sh=st
        while temp!=None:
            if temp.val<x:
                st.next=temp
                st=st.next
            else:
                tail.next=temp
                tail=tail.next
            temp=temp.next
        tail.next=None
        st.next=th.next
        return sh.next
            




        