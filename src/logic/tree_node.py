class Node:
    _id_counter = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

        self.id = Node._id_counter  # assign unique id
        Node._id_counter += 1
