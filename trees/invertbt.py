def invertbinarytree(root):
    if root is None:
        return None
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    # Recursively invert the left and right subtrees
    invertbinarytree(root.left)
    invertbinarytree(root.right)
    return root



# Example usage:
if __name__ == "__main__":
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    # Creating a binary tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # Inverting the binary tree
    invertbinarytree(root)

    # Function to print the tree in-order for verification
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            print(node.value, end=" ")
            inorder_traversal(node.right)

    # Printing the inverted binary tree
    inorder_traversal(root)  # Output should reflect the inverted structure