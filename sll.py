class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class sll:
    def __init__(self):
        self.head=None

    def insert_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def display(self):
        temp=self.head
        if self.head is None:
            print("empty list")
            return
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

l1=sll()

l1.insert_beg(10)
l1.insert_beg(5)
l1.insert_beg(13)
l1.insert_beg(7)

l1.display()


