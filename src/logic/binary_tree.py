from src.logic.tree_node import Node

# ============================================
# Binary Tree Class
# ============================================
class BinaryTree:
    """A binary tree data structure allowing flexible node placement."""
    
    def __init__(self, root_value=None):
        """Initializes the Binary Tree.

        Parameters:
            root_value (any, optional): The initial value for the root node. Defaults to None.
        """
        self.root = Node(root_value) if root_value is not None else None


    # -----------------------------------------
    # INSERTIONS
    # -----------------------------------------
    def insert_left(self, current_node, value):
        """Inserts a new node as the left child of the current node.

        Parameters:
            current_node (Node): The parent node.
            value (any): The value to insert.

        Returns:
            bool: True if insertion was successful, False if the left child already exists.
        """
        if current_node.left is not None:
            return False  # parent already has a left child
        current_node.left = Node(value)
        return True


    def insert_right(self, current_node, value):
        """Inserts a new node as the right child of the current node.

        Parameters:
            current_node (Node): The parent node.
            value (any): The value to insert.

        Returns:
            bool: True if insertion was successful, False if the right child already exists.
        """
        if current_node.right is not None:
            return False  # parent already has a right child
        current_node.right = Node(value)
        return True



    # -----------------------------------------
    # TRAVERSALS
    # -----------------------------------------
    def preorder_traversal(self, start, traversal):
        """Traverse the tree in preorder: root → left → right.

        Parameters:
            start (Node): The node to start traversing from.
            traversal (str): The accumulated traversal string.

        Returns:
            str: The updated traversal string.
        """
        if start:
            traversal += str(start.data) + " "
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal


    def inorder_traversal(self, start, traversal):
        """Traverse the tree in inorder: left → root → right.

        Parameters:
            start (Node): The node to start traversing from.
            traversal (str): The accumulated traversal string.

        Returns:
            str: The updated traversal string.
        """
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += str(start.data) + " "
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal


    def post_traversal(self, start, traversal):
        """Traverse the tree in postorder: left → right → root.

        Parameters:
            start (Node): The node to start traversing from.
            traversal (list): The list to append values to.

        Returns:
            list: The updated list of traversed values.
        """
        if start:
            traversal = self.post_traversal(start.left, traversal)
            traversal = self.post_traversal(start.right, traversal)
            traversal.append(start.data)
        return traversal

    def search(self, root, key):
        """Search by node id (used for insert/delete).

        Parameters:
            root (Node): The current node being checked.
            key (int): The unique ID of the node to find.

        Returns:
            Node or None: The node if found, otherwise None.
        """
        if root is None:
            return None
        if root.id == key:
            return root

        left = self.search(root.left, key)
        if left:
            return left

        return self.search(root.right, key)

    def search_by_value(self, root, value):
        """Return the first node with the given data, or None if not found.

        Parameters:
            root (Node): The current node being checked.
            value (any): The data value to search for.

        Returns:
            Node or None: The found node, or None.
        """
        if root is None:
            return None
        if str(root.data) == str(value):
            return root
        left_result = self.search_by_value(root.left, value)
        if left_result:
            return left_result
        return self.search_by_value(root.right, value)


    # -----------------------------------------
    # DELETE NODE
    # -----------------------------------------
    def find_min(self, root):
        """Finds the leftmost (minimum) node in the subtree.

        Parameters:
            root (Node): The root of the subtree.

        Returns:
            Node: The leftmost node.
        """
        while root.left:
            root = root.left
        return root

    
    def get_deepest_node(self, root):
        """Return the deepest (last) node and its parent.

        Parameters:
            root (Node): The root of the tree.

        Returns:
            tuple: (last_node, parent) or (None, None) if empty.
        """
        if not root:
            return None, None

        queue = [(root, None)]  # (node, parent)
        last_node, parent = None, None

        while queue:
            last_node, parent = queue.pop(0)
            if last_node.left:
                queue.append((last_node.left, last_node))
            if last_node.right:
                queue.append((last_node.right, last_node))
        
        return last_node, parent

    def delete(self, root, target_id):
        """Deletes a node by replacing it with the deepest node in the tree.

        Parameters:
            root (Node): The root of the tree.
            target_id (int): The unique ID of the node to delete.

        Returns:
            Node or None: The root of the modified tree.
        """
        if not root:
            return None

        # If tree has only one node
        if root.left is None and root.right is None:
            if root.id == target_id:
                return None
            else:
                return root

        # Find node to delete
        queue = [root]
        node_to_delete = None

        while queue:
            node = queue.pop(0)
            if node.id == target_id:
                node_to_delete = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if node_to_delete is None:
            return root  # node not found

        # Get deepest node
        deepest, parent_of_deepest = self.get_deepest_node(root)

        # Replace target node's data & id with deepest node
        node_to_delete.data = deepest.data
        node_to_delete.id = deepest.id

        # Remove the deepest node from its parent
        if parent_of_deepest.left == deepest:
            parent_of_deepest.left = None
        else:
            parent_of_deepest.right = None

        return root


    def find_parent(self, root, target_id, parent=None):
        """Finds the parent of a specific node.

        Parameters:
            root (Node): The current node being checked.
            target_id (int): The ID of the child node.
            parent (Node, optional): The parent of the current node.

        Returns:
            tuple: (parent_node, side) where side is "left" or "right".
        """
        if root is None:
            return None, None
        if root.id == target_id:
            # determine if left or right child
            if parent:
                if parent.left == root:
                    return parent, "left"
                elif parent.right == root:
                    return parent, "right"
            return parent, None
        
        left_parent, side = self.find_parent(root.left, target_id, root)
        if left_parent:
            return left_parent, side

        return self.find_parent(root.right, target_id, root)