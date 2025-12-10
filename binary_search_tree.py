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

    def max_value(self, node):
        """Return the maximum value in a BST."""
        if node is None:
            return None
        current = node
        while current.right is not None:
            current = current.right
        return current.data
    
    def min_value(self, node): # needed for delete function
        if node is None:
            return None
        current = node 
        while current.left is not None:
            current = current.left
        return current.left
    
    def delete(self, node, value):
        if node is None:
            return node
        if node.data > value:
            self.delete(node.left, value)
        elif node.data < value:
            self.delete(node, value)
        else:
            minimum_value = self.min_value(node)
            node.data = minimum_value.data
            node.right = self.delete(node.right,minimum_value.data)

        return node


    def find_height(self, node):
        if node is None:
            return 0
        left = self.find_height(node.left)
        right = self.find_height(node.right)
        return max(left, right) + 1  # finds each level until left or right is None and then picks the higher number
                  


