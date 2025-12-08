from tree_node import Node

# ============================================
# Binary Search Tree Class
# ============================================
class BinarySearchTree:
    """A binary search tree (BST) data structure."""

    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    # -----------------------------------------
    # INSERTION
    # -----------------------------------------
    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = Node(value)
            return True
        return self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value == node.data:
            return False  # No duplicates allowed
        elif value < node.data:
            if node.left is None:
                node.left = Node(value)
                return True
            else:
                return self._insert_recursive(node.left, value)
        else:  # value > node.data
            if node.right is None:
                node.right = Node(value)
                return True
            else:
                return self._insert_recursive(node.right, value)

    # -----------------------------------------
    # SEARCH
    # -----------------------------------------
    def search(self, value):
        """Return the node containing the value, or None."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None:
            return None
        if value == node.data:
            return node
        elif value < node.data:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    # -----------------------------------------
    # TRAVERSALS
    # -----------------------------------------
    def inorder_traversal(self, node=None):
        """Left → Root → Right"""
        if node is None:
            node = self.root
        if node is None:
            return ""  # empty tree
        return (
            self.inorder_traversal(node.left) +
            str(node.data) + " " +
            self.inorder_traversal(node.right)
        )

    def preorder_traversal(self, node=None):
        """Root → Left → Right"""
        if node is None:
            node = self.root
        if node is None:
            return ""
        return (
            str(node.data) + " " +
            self.preorder_traversal(node.left) +
            self.preorder_traversal(node.right)
        )

    def postorder_traversal(self, node=None):
        """Left → Right → Root"""
        if node is None:
            node = self.root
        if node is None:
            return ""
        return (
            self.postorder_traversal(node.left) +
            self.postorder_traversal(node.right) +
            str(node.data) + " "
        )


    # -----------------------------------------
    # DELETE NODE
    # -----------------------------------------
    def delete(self, value):
        """Delete a node by value."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.data:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.data:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node found
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data
            node.right = self._delete_recursive(node.right, min_larger_node.data)

        return node

    def _find_min(self, node):
        """Find the node with the minimum value in a subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current
