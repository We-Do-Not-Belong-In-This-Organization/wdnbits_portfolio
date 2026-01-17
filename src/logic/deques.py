from src.logic.node import Node


class Deque:
    """A Double-Ended Queue (Deque) allowing insertion and removal from both ends."""

    def __init__(self):
        """Initializes an empty Deque."""
        self.head = None
        self.tail = None

    def __iter__(self):
        """Iterates through the deque from front to rear.

        Yields:
            any: The data of each node in the deque.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def enqueue_front(self, data):  # Insert at front
        """Adds an item to the front of the deque.

        Parameters:
            data (any): The value to add.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def enqueue_rear(self, data):  # Insert at end
        """Adds an item to the rear of the deque.

        Parameters:
            data (any): The value to add.
        """
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue_front(self):  # Remove at front
        """Removes and returns the item from the front of the deque.

        Returns:
            any or None: The data at the front, or None if empty.
        """
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
        """Removes and returns the item from the rear of the deque.

        Returns:
            any or None: The data at the rear, or None if empty.
        """
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
        """Checks if the deque is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return self.head is None


    # Remove at specific part
    def remove_at(self, position):  # Remove node at a specific index (0-based)
        """Removes and returns the item at a specific index.

        Parameters:
            position (int): The 0-based index of the item to remove.

        Returns:
            any or None: The data at the index, or None if the index is invalid.
        """
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
        """Removes all elements from the deque."""
        self.head = None
        self.tail = None


    def length(self):  # Count length of deque
        """Returns the number of items in the deque.

        Returns:
            int: The total count of items.
        """
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count


    def display(self):  # Show all elements
        """Returns a list of all items in the deque for display.

        Returns:
            list: A list containing all data elements.
        """
        items = []
        current_node = self.head
        while current_node:
            items.append(current_node.data)
            current_node = current_node.next
        return items