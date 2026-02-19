# Node class represents each element of the linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data      # stores value
        self.next = next      # points to next node

# LinkedList class manages the linked list operations
class LinkedList:
    def __init__(self):
        self.head = None      # initially list is empty

    # Insert new node at the beginning
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    # Print all elements of the linked list
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr is not None:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    # Insert new node at the end
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = Node(data, None)
    
    #insert mulitple values
    def insert_values(self,data_list):
        # self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        
        return count
    
    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        
        if self.head==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        
        if self.head==0:
            self.insert_at_begining(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            itr=itr.next
            count+=1
        
# Example usage
ll = LinkedList()
ll.insert_at_begining(5)
ll.insert_at_begining(2)
ll.insert_at_end(99)
ll.insert_values(["apple","banana","carrot"])
print(ll.get_length())
# ll.remove_at(2)
ll.insert_at(2,55)
ll.print()
