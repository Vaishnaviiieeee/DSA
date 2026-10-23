
# Circular Queue using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class CQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node
        self.rear.next = self.front                     #added for circular       

    def dequeue(self):
        if self.front:                   #At least one node in the queue
            temp=self.front
            if self.front == self.rear:                       #updated for circular
              self.rear = self.rear = None                          #Updated for circular
              print("Now Queue is empty.")
            else:
              self.front= self.front.next
              self.rear.next = self.front
            temp = None 
        else:
            print("Queue is empty")            

    def print(self):
        temp = self.front
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.front:                 #Added for circular
                break                                 #Added for circular
        print()


que = CQueue()

que.enqueue(Node(15))
que.enqueue(Node(24))
que.enqueue(Node(74))
que.enqueue(Node(20))

que.print()
que.dequeue()
que.print()

