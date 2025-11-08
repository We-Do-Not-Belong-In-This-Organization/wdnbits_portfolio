# queue_linkedlist.py
from node import Node

class Queues:
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
            return current_node.data
        return None

    def is_empty(self):
        return self.head is None

    def peek(self):
        if self.head:
            return self.head.data
        return None

    def display(self):
        items = []
        current_node = self.head
        while current_node:
            items.append(current_node.data)
            current_node = current_node.next
        return items
