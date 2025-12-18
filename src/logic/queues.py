from src.logic.node import Node


class Queue:
    """A First-In-First-Out (FIFO) queue data structure."""

    def __init__(self):
        """Initializes an empty Queue."""
        self.head = None
        self.tail = None

    def __iter__(self):
        """Iterates through the queue from front to rear.

        Yields:
            any: The data of each node.
        """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def enqueue(self, data):  # Insert at end
        """Adds an item to the rear of the queue.

        Parameters:
            data (any): The value to add.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):  # Remove at front
        """Removes and returns the item from the front of the queue.

        Returns:
            any or None: The data at the front, or None if empty.
        """
        if self.head:
            current_node = self.head
            self.head = current_node.next
            current_node.next = None

            if self.head is None:
                self.tail = None
            return current_node.data
        return None

    def is_empty(self):  # Check if empty
        """Checks if the queue is empty.

        Returns:
            bool: True if empty, False otherwise.
        """
        return self.head is None

    def peek(self):  # Show front element
        """Returns the item at the front without removing it.

        Returns:
            any or None: The data at the front, or None if empty.
        """
        if self.head:
            return self.head.data
        return None

    def display(self):  # Show all elements
        """Returns a list of all items in the queue for display.

        Returns:
            list: A list containing all data elements.
        """
        items = []
        current_node = self.head
        while current_node:
            items.append(current_node.data)
            current_node = current_node.next
        return items

    # Remove at specific part (by index)
    def remove_at(self, position):
        """Removes an item at a specific index.

        Parameters:
            position (int): The 0-based index of the item to remove.

        Returns:
            any or None: The removed data, or None if index is invalid.
        """
        if self.is_empty():
            return None

        # Remove first element
        if position == 0:
            return self.dequeue()

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
        """Removes all elements from the queue."""
        self.head = None
        self.tail = None

    def length(self):  # Count total elements
        """Returns the number of items in the queue.

        Returns:
            int: The total count of items.
        """
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count