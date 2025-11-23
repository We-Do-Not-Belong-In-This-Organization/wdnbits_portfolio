from tree_node import Node


class BinaryTree:
    def post_traversal(self, start, traversal):
        if start:
            traversal = self.post_traversal(start.left, traversal) 
            traversal = self.post_traversal(start.right, traversal)
            traversal.append(start.data)
        return traversal


# Build a larger tree
tree = BinaryTree()

root = Node(10)
root.left = Node(5)
root.right = Node(15)

root.left.left = Node(2)
root.left.right = Node(7)

root.right.left = Node(12)
root.right.right = Node(20)

# Test post-order traversal
result = tree.post_traversal(root, [])
print(result)
