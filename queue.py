
# Linear Queue using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front:
          temp=self.front
          self.front = self.front.next
          if self.front == None:
              self.rear = None
              print("Now Queue is empty.")
          temp = None 
        else:
            print("Queue is empty")          

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()


que = LQueue()

que.enqueue(Node(15))
que.enqueue(Node(24))
que.enqueue(Node(74))
que.enqueue(Node(20))
que.enqueue(Node(39))
que.enqueue(Node(84))

que.print()
que.dequeue()
que.print()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()

que.print()
que.dequeue()
que.enqueue(Node(28))
que.enqueue(Node(19))
que.print()