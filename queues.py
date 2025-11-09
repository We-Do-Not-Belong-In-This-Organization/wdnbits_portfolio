# queues.py

from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def enqueue(self, data):  # Insert at end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):  # Remove at front
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

            if self.head is None:
                self.tail = None
            return current_node.data
        return None

    def is_empty(self):  # Check if empty
        return self.head is None

    def peek(self):  # Show front element
        if self.head:
            return self.head.data
        return None

    def display(self):  # Show all elements
        items = []
        current_node = self.head
        while current_node:
            items.append(current_node.data)
            current_node = current_node.next
        return items

    # Remove at specific part (by index)
    def remove_at(self, position):
        if self.is_empty():
            return None

        # Remove first element
        if position == 0:
            return self.dequeues()

        index = 0
        prev_node = None
        current_node = self.head

        while current_node and index < position:
            prev_node = current_node
            current_node = current_node.next
            index += 1

        # If found
        if current_node:
            data = current_node.data
            prev_node.next = current_node.next

            # Update tail if last node is removed
            if current_node == self.tail:
                self.tail = prev_node

            current_node.next = None
            return data

        return None  # position out of range

    def clear(self):  # Clear all elements
        self.head = None
        self.tail = None

    def length(self):  # Count total elements
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
