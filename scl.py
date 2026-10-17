from abc import ABC, abstractmethod


class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class AbstractList(ABC):
    @abstractmethod
    def append(self, new_node):
        """Add a node to the end of the list."""
        raise NotImplementedError

    @abstractmethod
    def insert(self, *args):
        """Insert a node at a valid position in the list."""
        raise NotImplementedError

    @abstractmethod
    def print(self):
        """Print every node in the list."""
        raise NotImplementedError


class SLL(AbstractList):
    def __init__(self):
        self.head = None

    def _to_list(self):
        if self.head is None:
            return []

        nodes = []
        temp = self.head
        while True:
            nodes.append(temp)
            temp = temp.next
            if temp == self.head:
                break
        return nodes

    def append(self, new_node):
        if not isinstance(new_node, Node):
            raise TypeError("append expects a Node object")

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        nodes = self._to_list()
        nodes.append(new_node)

        for index in range(len(nodes) - 1):
            nodes[index].next = nodes[index + 1]
        nodes[-1].next = self.head

    def insert(self, *args):
        if not args:
            raise TypeError("insert requires a node and a position")

        if len(args) == 2:
            first, second = args
            if isinstance(first, int):
                pos, new_node = first, second
            else:
                new_node, pos = first, second
        elif len(args) == 3:
            if isinstance(args[0], int):
                pos, new_node = args[0], args[1]
            else:
                new_node, pos = args[0], args[1]
        else:
            raise TypeError("insert accepts either (new_node, pos) or (pos, new_node)")

        if not isinstance(new_node, Node):
            raise TypeError("insert expects a Node object")

        if pos < 1:
            raise IndexError("Position must be 1 or greater")

        if self.head is None:
            if pos != 1:
                raise IndexError("List is empty; insertion position must be 1")
            self.head = new_node
            new_node.next = new_node
            return

        nodes = self._to_list()

        if pos > len(nodes) + 1:
            raise IndexError("Insertion position is out of range")

        nodes.insert(pos - 1, new_node)

        for index in range(len(nodes) - 1):
            nodes[index].next = nodes[index + 1]
        nodes[-1].next = nodes[0]
        self.head = nodes[0]

    def print(self):
        if self.head is None:
            print("\nList is empty")
            return

        print()
        temp = self.head
        print("List elements:")
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()


# Execution
list1 = SLL()
n1 = Node(10)
n2 = Node(20)
list1.append(n1)
list1.append(n2)
list1.append(Node(30))
list1.append(Node(40))
list1.print()  # Output: 10 20 30 40

list1.insert(Node(34), 1)
list1.print()  # Output: 34 10 20 30 40

list1.insert(1, Node(58), 1)
list1.print()  # Output: 58 34 10 20 30 40

list1.delete(10)
list1.print()  # Output: 58 34 20 30 40