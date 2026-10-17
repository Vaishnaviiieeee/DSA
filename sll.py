#Singly Linked List

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
class SLL:
    def __init__(self):
        self.head=None
    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next):
                temp=temp.next
            temp.next=new_node
    def print(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            
    def del_node(self,value):
        prev.next=temp.next
        temp=None

    def insert(self,new_node,pos):
        if pos==1:# insert node at first position
            new.node.next=self.head
            self.head=new_node
        else: #insert node from 2nd to last position
            p=1
            temp=self.head
            while(p!=pos-1):
                temp(p!=pos-1)
                temp=temp.next
                p+=1
            
list1=SLL()
n1=Node(10)
n2=Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
# list1.append(Node(55))
# list1.append(Node(65))
# list1.append(Node(25))
list1.print()

