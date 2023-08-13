from typing import Optional
from BinaryTree import TreeNode, Tree, print_tree



# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.


# Recursive Solution
def maxDepth(root: Optional[TreeNode]) -> int:
    if root == None:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))





if __name__ == "__main__":
    root = [3,9,20, None, None,15,7]
    tree = Tree()
    tree.createFromListBFS(root)
    k = maxDepth(tree.root)
    print_tree(tree.root)

    print(k)