
# Assessment 3.3
# Non-linear Data Structure
# Student: JABERINA
# Program: Binary Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Create Binary Tree
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)


# Inorder Traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


# Preorder Traversal
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder Traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


print("================================")
print("   JABERINA - BINARY TREE")
print("================================")

print("\nInorder Traversal:")
inorder(root)

print("\n\nPreorder Traversal:")
preorder(root)

print("\n\nPostorder Traversal:")
postorder(root)

print("\n================================")
