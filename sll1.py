class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singlelinkedlist:
    def __init__(self):
        self.head=None

    def insert_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        if self.head is None:
            print("list is empty")
            return
        
        temp=self.head

        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

    def insert_end(self,data):
        if self.head is None:
            self.insert_beg(data)
            return
        
        new_node=Node(data)

        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

    def insert_after(self,data,x):
        temp=self.head

        while temp is not None:
            if temp.data==x:
                break
            temp=temp.next
        if temp is None:
            print("empty")
        else:
            new_node = Node(data)
            new_node.next=temp.next
            temp.next=new_node

    def insert_before(self,data,x):
        if self.head is None:
            print("empty")
            return
        if self.head.data==x:
            self.insert_beg(data)
            return
        temp=self.head
        while temp.next is not None:
            if temp.next.data==x:
                break
            temp=temp.next

        if temp.next is None:
            print("empty")
        else:
            new_node=Node(data)
            new_node.next=temp.next
            temp.next=new_node
        


o1=singlelinkedlist()

o1.insert_beg(10)
o1.insert_beg(16)
o1.insert_beg(5)
o1.insert_beg(2)

o1.insert_end(8)
o1.insert_end(3)
o1.insert_end(4)

o1.insert_after(9,8)

o1.insert_before(1,8)
o1.insert_before(2,9)



o1.display()
        