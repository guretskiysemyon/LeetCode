'''
Author: Semyon Guretskiy
'''


'''
Given the root of a binary tree, invert the tree, and return its root.
      4                   4
    2     7     -->     7      2
  1   3  6  9         9   6  3    1

Link: https://leetcode.com/problems/invert-binary-tree/description/
'''




from typing import Optional
from BinaryTree import TreeNode, Tree


# Swap left and right in post-order traversal.
def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None:
        return None

    invertTree(root.left)
    invertTree(root.right)
    temp = root.left
    root.left = root.right
    root.right = temp
    return root


if __name__ == "__main__":
    root = [4,2,7,1,3,6,9]
    tree = Tree()
    tree.createFromListBFS(root)
    tree.print_tree(tree.root)
    invertTree(tree.root)
    tree.print_tree(tree.root)