def sametree(tree1, tree2):
    """Check if two binary trees are identical in structure and node values."""
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    if tree1.value != tree2.value:
        return False
    return (sametree(tree1.left, tree2.left) and 
            sametree(tree1.right, tree2.right))

# Example usage:
if __name__ == "__main__":
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    # Creating two identical binary trees:
    #       1
    #      / \
    #     2   3
    tree1 = TreeNode(1)
    tree1.left = TreeNode(2)
    tree1.right = TreeNode(3)

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)

    # Creating a different binary tree:
    #       1
    #      / \
    #     2   4
    tree3 = TreeNode(1)
    tree3.left = TreeNode(2)
    tree3.right = TreeNode(4)

    print(sametree(tree1, tree2))  # Output: True
    print(sametree(tree1, tree3))  # Output: False