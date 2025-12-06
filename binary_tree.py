from tree_node import Node

# ============================================
# Binary Tree Class
# ============================================
class BinaryTree:
    """A binary tree data structure."""
    
    def __init__(self, root_value=None):
        self.root = Node(root_value) if root_value is not None else None


    # -----------------------------------------
    # INSERTIONS
    # -----------------------------------------
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


    # -----------------------------------------
    # TRAVERSALS
    # -----------------------------------------
    def preorder_traversal(self, start, traversal):
        """Traverse the tree in preorder: root → left → right."""
        if start:
            traversal += str(start.data) + " "
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal


    def inorder_traversal(self, start, traversal):
        """Traverse the tree in inorder: left → root → right."""
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += str(start.data) + " "
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal


    def post_traversal(self, start, traversal):
        """Traverse the tree in postorder: left → right → root."""
        if start:
            traversal = self.post_traversal(start.left, traversal)
            traversal = self.post_traversal(start.right, traversal)
            traversal.append(start.data)
        return traversal

    def search(self, root, key):
        while root:
            if root.data == key:
                return True
            else:
                self.search(root.right, key)

    def search_by_id(self, root, node_id):
        if root is None:
            return None
        if root.id == node_id:
            return root

        left = self.search_by_id(root.left, node_id)
        if left:
            return left

        return self.search_by_id(root.right, node_id)

    # -----------------------------------------
    # DELETE NODE
    # -----------------------------------------
    def delete_node(self, root, key):
        """Delete a node from a general binary tree."""
        if root is None:
            return None

        # Case: only one node
        if root.data == key and root.left is None and root.right is None:
            return None

        target = None
        last = None
        queue = [root]

        # Perform BFS search
        while queue:
            last = queue.pop(0)

            if last.data == key:
                target = last

            if last.left:
                queue.append(last.left)

            if last.right:
                queue.append(last.right)

        # If target node does not exist
        if target is None:
            return root

        # Replace target node's data with deepest node's data
        target.data = last.data

        # Remove deepest node
        self._delete_deepest(root, last)

        return root


    # Helper to delete deepest node
    def _delete_deepest(self, root, dnode):
        queue = [root]

        while queue:
            temp = queue.pop(0)

            if temp.left:
                if temp.left is dnode:
                    temp.left = None
                    return
                queue.append(temp.left)

            if temp.right:
                if temp.right is dnode:
                    temp.right = None
                    return
                queue.append(temp.right)

    def find_parent(root, target_id, parent=None):
        if root is None:
            return None, None
        if root.id == target_id:
            return parent, "left" if parent and parent.left == root else "right"
        
        left = find_parent(root.left, target_id, root)
        if left[0]:
            return left

        return find_parent(root.right, target_id, root)

