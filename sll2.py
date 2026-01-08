class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class sll2:
    def __init__(self):
        self.head = None

    def ins_beg(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def ins_end(self,data):
        
        if self.head is None:
            self.ins_beg(data)
            return
        temp=self.head
        new_node=Node(data)

        while temp.next is not None:
            temp=temp.next
        temp.next=new_node

    def ins_after(self,data,x):
        
        temp=self.head
        while temp is not None:
            if temp.data==x:
                break
            temp=temp.next
        if temp is None:
            return "empty"
        new_node=Node(data)
        new_node.next=temp.next
        temp.next=new_node

    def ins_before(self,data,x):
        temp=self.head
        while temp.next is not None:
            if temp.next.data==x:
                break
            temp=temp.next
        if temp.next is None:
            return "empty"
        new_node=Node(data)
        new_node.next=temp.next
        temp.next=new_node
    

    def display(self):
        temp=self.head
        if self.head is None:
            return "empty"
        
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
        print("None")

o1=sll2()

o1.ins_beg(1)
o1.ins_beg(2)
o1.ins_beg(3)

o1.ins_end(4)

o1.ins_after(5,1)

o1.ins_before(6,5)

o1.display()

        
        
        