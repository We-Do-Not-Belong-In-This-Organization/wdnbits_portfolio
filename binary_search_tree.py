# binary_search_tree.py

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """Binary Search Tree (BST)"""

    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def search_bst(self, node, value):
        """Search for a value in a BST."""
        if node is None:
            return False
        if node.data == value:
            return True
        if value < node.data:
            return self.search_bst(node.left, value)
        else:
            return self.search_bst(node.right, value)

    def get_max_value(self, node):
        """Return the maximum value in a BST."""
        if node is None:
            return None
        current = node
        while current.right is not None:
            current = current.right
        return current.data
