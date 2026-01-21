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
    def inorder_traversal(self):
        """Public wrapper: returns a string for whole tree (left, root, right)."""
        return self._inorder(self.root).strip()

    def _inorder(self, node):
        if node is None:
            return ""
        return (
            self._inorder(node.left) +
            str(node.data) + " " +
            self._inorder(node.right)
        )

    def preorder_traversal(self):
        """Public wrapper: root, left, right."""
        return self._preorder(self.root).strip()

    def _preorder(self, node):
        if node is None:
            return ""
        return (
            str(node.data) + " " +
            self._preorder(node.left) +
            self._preorder(node.right)
        )

    def postorder_traversal(self):
        """Public wrapper: left, right, root."""
        return self._postorder(self.root).strip()

    def _postorder(self, node):
        if node is None:
            return ""
        return (
            self._postorder(node.left) +
            self._postorder(node.right) +
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
    
    def find_height(self, node):
        if node is None:
            return 0
        left = self.find_height(node.left)
        right = self.find_height(node.right)
        return max(left, right) + 1