class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class LinkedList:
    
    def __init__(self):
        self.head=None
    
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def print(self):
        
        itr=self.head
        result=''
        while itr:
            result+=str(itr.data) +'-->'
            itr=itr.next
        print(result)
        
        
    
    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return

        while itr:
            if itr.data==data_after:
                node=Node(data_to_insert,itr.next)
                itr.next=node
                break
            
            itr=itr.next
    def remove_by_value(self,data):
        
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        itr=self.head
        while itr.next:
            if itr.next.data==data:
                itr.next=itr.next.next
                break
            
            itr=itr.next
            
ex=LinkedList()
ex.insert_at_begining(34)
ex.insert_at_begining(3456)
ex.insert_at_begining(3)
ex.insert_at_begining(2224)
ex.insert_after_value(3,99)
ex.remove_by_value(34)
ex.print()