class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return

        temp = self.root
        while True:
            if new_node.data < temp.data:
                if temp.left is None:
                    temp.left = new_node
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return
                temp = temp.right

    def del_node(self, rt, val):
        if rt is None:
            return None

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)
        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)
        else:
            # Node with 0 or 1 child
            if rt.left is None:
                return rt.right
            if rt.right is None:
                return rt.left

            # Node with 2 children (indented inside 'else')
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    def get_successor(self, temp):
        temp = temp.right
        while temp is not None and temp.left is not None:
            temp = temp.left
        return temp

    def inorder(self, rt):
        if rt is None:
            return
        self.inorder(rt.left)
        print(rt.data, end=" ")
        self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        print(rt.data, end=" ")
        self.preorder(rt.left)   # Fixed: was self.inorder
        self.preorder(rt.right)  # Fixed: was self.inorder

    def postorder(self, rt):
        if rt is None:
            return
        self.postorder(rt.left)  # Fixed: was self.inorder
        self.postorder(rt.right) # Fixed: was self.inorder
        print(rt.data, end=" ")

    def search(self,key):
        temp = self.root
        while temp:
            if temp.data == key :
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False

    def findminmax(self):
        if self.root is None:
            print("\nTree is empty")
            return

        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin:", temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max:", temp.data)


# --- Driver Code ---
b1 = BST()
for val in [100, 10, 450, 4, 65, 300, 500]:
    b1.insert(Node(val))

print("Inorder:")
b1.inorder(b1.root)

print("\n\nPreorder:")
b1.preorder(b1.root)

print("\n\nPostorder:")
b1.postorder(b1.root)
print()

b1.findminmax()

# Reassign self.root so deleting the root node works properly
b1.root = b1.del_node(b1.root, 65)
print("\nAfter Delete:")
b1.inorder(b1.root)
if b1.search(500):
    print("\nfound node")
else:
    print("\n not found node")

if b1.search(5):
    print("\nfound node")
else:
    print("\nnot found node")