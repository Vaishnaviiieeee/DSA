
# (Binary Search Tree) BST

# Example 1:
# 27, 14, 19, 35, 31, 10, 42, 15, 55, 92, 50, -3

# Inorder: Left.Root.Right
# -3, 10, 14, 15, 19, 27, 31, 35, 42, 50, 55, 92

# Preorder: Root.Left subtree.Right subtree
# 27, 14, 10, -3, 19, 15, 35, 31, 42, 55, 50, 92

# Postorder: Left subtree.Right subtree.Root
# -3, 10, 15, 19, 14, 31, 50, 92, 55, 42, 35, 27


# Example 2:
# 75, 34, 45, 62, 22, 96, 82, 105, 98, 25

# INORDER:
# 22, 25, 34, 45, 62, 75, 82, 96, 98, 105

# PREORDER:
# 75, 34, 22, 25, 45, 62, 96, 82, 105, 98

# POSTORDER:
# 22, 25, 34, 45, 62, 75, 82, 96, 98, 105


# CONSTRUCT BST WITH FOLLOWING TRAVERSAL:

# INORDER:
# 3, 5, 8, 15, 20, 24, 37, 50, 58, 60, 62, 91

# POSTORDER:
# 3, 8, 5, 24, 37, 20, 15, 60, 58, 91, 62, 50

# BST:
# 50, 3, 8, 5, 24, 37, 20, 15, 60, 58, 91, 62


# NODE CLASS

class node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


# BST CLASS

class BST:
    def __init__(self):
        self.root = None
        self.cnt = 0

    # INSERT NODE

    def insert(self, new_node):
        if self.root is None:  # BST is empty
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                else:  # Right subtree
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right

    # INORDER TRAVERSAL OF BST

    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            if rt.left is None and rt.right is None:
                self.cnt +=1
            print(rt.data, end=" ")
            self.inorder(rt.right)

    # PREORDER TRAVERSAL

    def preorder(self, rt):
        if rt is None:
            return

        print(rt.data, end=" ")
        self.preorder(rt.left)
        self.preorder(rt.right)

    def count_nleaf(self, rt): 
        if rt is None:
            return
        else:
            self.count_nleaf(rt.left)
            if rt.left is not None or rt.right is not None:
                self.cnt +=1
            self.count_leaf(rt.right)


    # DELETE NODE FROM BST

    def del_node(self, rt, val):
        if rt is None:
            return

        if val < rt.data:
            rt.left = self.del_node(rt.left, val)

        elif val > rt.data:
            rt.right = self.del_node(rt.right, val)

        else:
            if rt.left is None:
                return rt.right

            if rt.right is None:
                return rt.left

            # When node has both left and right child
            succ = self.get_successor(rt)
            rt.data = succ.data
            rt.right = self.del_node(rt.right, succ.data)

        return rt

    # GET SUCCESSOR

    def get_successor(self, temp):
        temp = temp.right

        while temp is not None and temp.left is not None:
            temp = temp.left

        return temp

# Searching a node in BST
    def search(self, key):
        temp = self.root
        while temp:
            if temp.data == key:
                return True
            elif key < temp.data:
                temp = temp.left
            else:
                temp = temp.right
        return False


# CREATE BST

b1 = BST()

b1.insert(node(100))
b1.insert(node(10))
b1.insert(node(450))
b1.insert(node(4))
b1.insert(node(0))
b1.insert(node(65))
b1.insert(node(300))
b1.insert(node(500))


# INORDER TRAVERSAL

print("Inorder traversal of BST:", end=" ")
b1.inorder(b1.root)


# FIND MIN AND MAX IN BST

def find_min(self, rt):  # MIN
    if rt is None:
        return None

    while rt.left is not None:
        rt = rt.left

    return rt.data


def find_max(self, rt):  # MAX
    if rt is None:
        return None

    while rt.right is not None:
        rt = rt.right

    return rt.data


print("\nMinimum value in BST:", find_min(b1, b1.root))
print("Maximum value in BST:", find_max(b1, b1.root))


# PREORDER TRAVERSAL

print("\nPreorder traversal of BST:", end=" ")
b1.preorder(b1.root)

# DELETING NODE FROM BST

print("\nDeleting node from BST:")

b1.root = b1.del_node(b1.root, 4)

b1.inorder(b1.root)

if b1.search(65):
    print("\nFound the node")
else:
    print("\nNode not found)")

print("\nTotal leaf nodes in BST:", b1.cnt)

b1.count_nleaf(b1.root)
print("\nTotal non-leaf nodes in BST:", b1.cnt)

# COUNTING LEAF NODE
# COUNTING NON-LEAF NODE
# COUNTING TOTAL NODE

# STACK
# QUEUE
# LINKED LIST
