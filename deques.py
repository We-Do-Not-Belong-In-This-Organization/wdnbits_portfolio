from node import Node

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def enqueue_front(self, data):  # Insert at front
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def enqueue_rear(self, data):  # Insert at end
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue_front(self):  # Remove at front
        if self.head:
            data = self.head.data
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

            if self.head is None:
                self.tail = None
            return data
        return None

    def dequeue_rear(self):  # Remove at end
        if self.tail:
            data = self.tail.data
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                while current_node.next != self.tail:
                    current_node = current_node.next
                current_node.next = None
                self.tail = current_node
            return data
        return None

    def is_empty(self):  # Check if empty
        return self.head is None


    # Remove at specific part
    def remove_at(self, position):  # Remove node at a specific index (0-based)
        if self.is_empty():
            return None

        if position == 0:
            return self.dequeue_front()

        index = 0
        prev_node = None
        current_node = self.head

        while current_node and index < position:
            prev_node = current_node
            current_node = current_node.next
            index += 1

        if current_node:
            data = current_node.data
            prev_node.next = current_node.next

            if current_node == self.tail:
                self.tail = prev_node

            current_node.next = None
            return data

        return None  # position out of range


    def clear(self):  # Clear all
        self.head = None
        self.tail = None


    def length(self):  # Count length of deque
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count


    def display(self):  # Show all elements
        items = []
        current_node = self.head
        while current_node:
            items.append(current_node.data)
            current_node = current_node.next
        return items
