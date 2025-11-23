from tree_node import Node


# Binary Tree
class BinaryTree:
    """A binary tree data structure."""
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None

    def insert_left(self, current_node, value):
        """Insert a node as the left child of the current node."""
        if current_node.left is None:
            current_node.left = Node(value)
        else:
            new_node = Node(value)
            new_node.left = current_node.left
            current_node.left = new_node

    def insert_right(self, current_node, value):
        """Insert a node as the right child of the current node."""
        if current_node.right is None:
            current_node.right = Node(value)
        else:
            new_node = Node(value)
            new_node.right = current_node.right
            current_node.right = new_node

    def preorder_traversal(self, start,traversal):
        """Traverse the tree in preorder (root, left, right)."""
        if start:
            traversal += (str(start.value) + " ")
            traversal = self.preorder_traversal(start.left,traversal)
            traversal = self.preorder_traversal(start.right,traversal)
        return traversal    

    def inorder_traversal(self, start,traversal):
        """Traverse the tree in inorder (left, root, right)."""
        if start:
            traversal = self.inorder_traversal(start.left,traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_traversal(start.right,traversal)
        return traversal    
    
    def post_traversal(self, start, traversal):
        """Traverse the tree in postorder (left, root, right)."""
        if start:
            traversal = self.post_traversal(start.left, traversal) 
            traversal = self.post_traversal(start.right, traversal)
            traversal.append(start.data)
        return traversal

    def search(self, root, key):
        """Search for a value in the tree."""
        pass

    def delete_node(self, root, key):
        """Delete a node with the given value from the tree."""
        pass


# Build a larger tree
tree = BinaryTree()

root = Node(10)
root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.left = Node(12)
root.right.right = Node(20)

# Test post-order traversal
result = tree.post_traversal(root, [])
print(result)
