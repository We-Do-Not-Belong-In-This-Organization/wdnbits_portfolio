class Node:
    """A node class for binary tree structures with unique identification."""
    
    _id_counter = 0

    def __init__(self, data):
        """Initializes a Tree Node with data and assigns a unique ID.

        Parameters:
            data (any): The value to store in the node.
        """
        self.data = data
        self.left = None
        self.right = None

        self.id = Node._id_counter  # assign unique id
        Node._id_counter += 1
        