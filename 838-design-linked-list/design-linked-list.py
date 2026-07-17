class Node:
    def __init__(self,val):
        self.next=None
        self.val=val
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
        

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        if self.head==None:
            return -1
        temp=self.head
        while index>0 and temp!=None:
            temp=temp.next
            index-=1
        if temp==None:
            return -1
        return temp.val

    def addAtHead(self, val: int) -> None:
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
            self.size+=1
            return
        new_node.next=self.head
        self.head=new_node
        self.size+=1
        
    def addAtTail(self, val: int) -> None:
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
            self.tail=self.head
            self.size+=1
            return
        self.tail.next=new_node
        self.tail=self.tail.next
        self.size+=1
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.size:
            return 
        temp=self.head
        new_node=Node(val)
        if index==0:
            return self.addAtHead(val)
        if index==self.size:
            return self.addAtTail(val)

        while temp!=None and index>1:
            temp=temp.next
            index-=1
        if temp==None:
            return 
        else:
            new_node.next=temp.next
            temp.next=new_node
        self.size+=1

        

    def deleteAtIndex(self, index: int) -> None:
        
        if index<0 or index>=self.size:
            return 
        temp=self.head
        if index==0:
            self.head=self.head.next
            if self.head is None:
                self.tail = None
            self.size-=1
            return
        
        while temp!=None and index>1:
            temp=temp.next
            index-=1
        if temp.next!=None:
            temp.next=temp.next.next
            if temp.next is None:
                self.tail = temp
            self.size-=1

       
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)