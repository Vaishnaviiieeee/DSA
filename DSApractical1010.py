def solution():
    class Node:
        def init(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def init(self):
            self.head = None

        def insert_end(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        def display(self):
            temp = self.head
            values = []
            while temp:
                values.append(str(temp.data))
                temp = temp.next
            print(" ".join(values))

        def insert_at_position(self, data, pos):
            new_node = Node(data)
            if pos == 1:
                new_node.next = self.head
                self.head = new_node
                return
            temp = self.head
            for _ in range(pos - 2):
                if temp is None:
                    return
                temp = temp.next
            if temp is None:
                return
            new_node.next = temp.next
            temp.next = new_node

        def find_middle(self):
            slow = fast = self.head
            if slow is None:
                return
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print(slow.data)

        def delete_node(self, value):
            temp = self.head
            if temp and temp.data == value:
                self.head = temp.next
                return
            while temp and temp.next:
                if temp.next.data == value:
                    temp.next = temp.next.next
                    return
                temp = temp.next

        def reverse(self):
            prev = None
            curr = self.head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            self.head = prev

        def consecutive_sums(self):
            temp = self.head
            sums = []
            while temp and temp.next:
                sums.append(temp.data + temp.next.data)
                temp = temp.next
            print(*sums)

    n = int(input())
    values = list(map(int, input().split()))

    ll = LinkedList()
    for value in values[:n]:
        ll.insert_end(value)

    ll.display()

    data = int(input())
    pos = int(input())
    ll.insert_at_position(data, pos)
    ll.display()

    ll.find_middle()

    value = int(input())
    ll.delete_node(value)
    ll.display()

    ll.reverse()
    ll.display()

    ll.consecutive_sums()


solution()