from node import Node

class Queues():
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueues(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeues(self):
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

            if self.head is None:
                self.tail = None
#di pa to tapos ata ewan ko - marx