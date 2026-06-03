# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        prev=None
        while temp!=None:
            kthnode=self.kth(temp,k)
            if kthnode==None:
                if prev:
                    prev.next=temp
                    break
            nextnode=kthnode.next
            kthnode.next=None
            self.reverse(temp)
            if temp==head:
                head=kthnode
            else:
                prev.next=kthnode
            prev=temp
            temp=nextnode
            
        return head
                
            
    def kth(self,head,k):
        temp=head
        ct=1
        while temp!=None and ct<k:
            temp=temp.next
            ct+=1
        return temp

    def reverse(self,head):
        curr=head
        next=head
        prev=None
        while curr!=None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev

        