class Node:
    """A basic node class for linked data structures."""

    def __init__(self, data):
        """Initializes a Node with data.

        Parameters:
            data (any): The value to store in the node.
        """
        self.data = data
        self.next = None
        