
# Linear Queue using Linked List and Stack

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


# Stack using Linked List
class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        else:
            popped_node = self.top
            self.top = self.top.next
            popped_node.next = None
            return popped_node

    def isempty(self):
        return self.top is None


# Linear Queue using Linked List
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
            dequed_node = self.front
            self.front = self.front.next

            if self.front is None:
                self.rear = None

            dequed_node.next = None
            return dequed_node
        else:
            print("Queue is empty")
            return None

    def isempty(self):
        return self.front is None

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()


# Reverse Queue using Stack
def reverse_queue(q1):
    st1 = Stack()

    while not q1.isempty():
        node = q1.dequeue()
        st1.push(Node(node.data))

    while not st1.isempty():
        node = st1.pop()
        q1.enqueue(Node(node.data))


# Main Program
que = LQueue()

que.enqueue(Node(15))
que.enqueue(Node(24))
que.enqueue(Node(74))
que.enqueue(Node(20))
que.enqueue(Node(39))
que.enqueue(Node(84))

print("Original Queue:")
que.print()

reverse_queue(que)

print("Reversed Queue:")
que.print()
