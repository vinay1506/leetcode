def subtreeofanother(tree1, tree2):
    """Check if tree2 is a subtree of tree1."""
    if not tree2:
        return True  # An empty tree is a subtree of any tree
    if not tree1:
        return False  # Non-empty tree cannot be a subtree of an empty tree

    def sametree(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        if t1.value != t2.value:
            return False
        return sametree(t1.left, t2.left) and sametree(t1.right, t2.right)

    if sametree(tree1, tree2):
        return True
    return subtreeofanother(tree1.left, tree2) or subtreeofanother(tree1.right, tree2)

# Example usage:
if __name__ == "__main__":      
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    # Creating tree1:
    #       3
    #      / \
    #     4   5
    #    / \
    #   1   2
    #      /
    #     0
    tree1 = TreeNode(3)
    tree1.left = TreeNode(4)
    tree1.right = TreeNode(5)
    tree1.left.left = TreeNode(1)
    tree1.left.right = TreeNode(2)
    tree1.left.right.left = TreeNode(0)

    # Creating tree2:
    #     4
    #    / \
    #   1   2
    tree2 = TreeNode(4)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(2)

    print(subtreeofanother(tree1, tree2))  # Output: True

    # Creating tree3:
    #     4
    #    / \
    #   1   2
    #        \
    #         0
    tree3 = TreeNode(4)
    tree3.left = TreeNode(1)
    tree3.right = TreeNode(2)
    tree3.right.right = TreeNode(0)

    print(subtreeofanother(tree1, tree3))  # Output: False