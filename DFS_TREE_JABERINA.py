from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_validated_name(prompt):
    while True:
        raw_input = input(prompt).strip()
        # Allow letters and spaces only; reject numbers, symbols, or empty input
        if not raw_input or not all(ch.isalpha() or ch.isspace() for ch in raw_input):
            print("Invalid input! Please enter letters only (no numbers or symbols).")
            continue
        cleaned = "".join(ch.upper() for ch in raw_input if ch.isalpha())
        if not cleaned:
            print("Invalid input! Please enter at least one letter.")
            continue
        return cleaned


def build_binary_tree_from_letters(letters):
    """Builds a level-order (BFS) binary tree dynamically from a list/string of letters."""
    if not letters:
        return None

    root = Node(letters[0])
    queue = deque([root])
    idx = 1

    while queue and idx < len(letters):
        current = queue.popleft()

        # Assign left child
        if idx < len(letters):
            current.left = Node(letters[idx])
            queue.append(current.left)
            idx += 1

        # Assign right child
        if idx < len(letters):
            current.right = Node(letters[idx])
            queue.append(current.right)
            idx += 1

    return root


def preorder_traversal(node, result):
    if node:
        result.append(node.data)
        preorder_traversal(node.left, result)
        preorder_traversal(node.right, result)


def inorder_traversal(node, result):
    if node:
        inorder_traversal(node.left, result)
        result.append(node.data)
        inorder_traversal(node.right, result)


def postorder_traversal(node, result):
    if node:
        postorder_traversal(node.left, result)
        postorder_traversal(node.right, result)
        result.append(node.data)


def main():
    print("=== Assessment 3.6: DFS Methods in Tree (Custom Name) ===")
    print("Tip: Enter your First Name and Last Name (e.g., Marc Colon)\n")

    while True:
        first_name = get_validated_name("Enter First Name: ")
        last_name = get_validated_name("Enter Last Name : ")
        combined_name = first_name + last_name

        print(f"\nBuilding Binary Tree using letters from: {first_name} {last_name} ({combined_name})")
        root = build_binary_tree_from_letters(combined_name)

        preorder_res = []
        inorder_res = []
        postorder_res = []

        preorder_traversal(root, preorder_res)
        inorder_traversal(root, inorder_res)
        postorder_traversal(root, postorder_res)

        print("-" * 45)
        print("PreOrder Traversal  :", " -> ".join(preorder_res))
        print("InOrder Traversal   :", " -> ".join(inorder_res))
        print("PostOrder Traversal :", " -> ".join(postorder_res))
        print("-" * 45)

        again = input("\nTest another name? (y/n): ").strip().lower()
        if again != "y":
            print("Done! Ready to push to GitHub.")
            break


if __name__ == "__main__":
    main()