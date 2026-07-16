class Node:
    def __init__(self,key,val):
        self.key=key
        self.value=val
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.d=defaultdict(Node)
        

    def get(self, key: int) -> int:
        if key in self.d:
            #delete that node
            node=self.d[key]
            node.prev.next=node.next
            node.next.prev=node.prev
            #insert that in front
            node.prev=self.head
            node.next=self.head.next
            self.head.next.prev=node
            self.head.next=node
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        #when full
        if key in self.d:
            #delete that node
            node=self.d[key]
            node.prev.next=node.next
            node.next.prev=node.prev
            #insert that in front
            node.prev=self.head
            node.next=self.head.next
            self.head.next.prev=node
            self.head.next=node
            node.value=value


        elif len(self.d)>=self.capacity:
            #remove the last one
            del self.d[self.tail.prev.key]
            self.tail.prev=self.tail.prev.prev
            self.tail.prev.next=self.tail
            #now add the new node after head
            new_node=Node(key,value)

            new_node.prev=self.head
            new_node.next=self.head.next
            self.head.next.prev=new_node
            self.head.next=new_node
            self.d[key]=new_node
        else:
            new_node=Node(key,value)

            new_node.prev=self.head
            new_node.next=self.head.next
            self.head.next.prev=new_node
            self.head.next=new_node
            self.d[key]=new_node



        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)