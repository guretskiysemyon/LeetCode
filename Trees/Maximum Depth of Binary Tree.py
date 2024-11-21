
'''
Author: Semyon Guretskiy
'''

'''
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

'''
from typing import Optional
from BinaryTree import TreeNode, Tree




# Recursive DFS
def maxDepthRecursive(root: Optional[TreeNode]) -> int:
    if root == None:
        return 0

    return 1 + max(maxDepthRecursive(root.left), maxDepthRecursive(root.right))

# Iterative DFS
def maxDepthIterative(root: Optional[TreeNode]) -> int:
    stack = [(root, 1)]

    result = -1

    while stack:
        node, depth = stack.pop()
        
        
        if node:
            if depth > result:
                result = depth
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    
    return result
    




if __name__ == "__main__":
    root = [3,9,20, None, None,15,7]
    tree = Tree()
    tree.createFromListBFS(root)
    k = maxDepthRecursive(tree.root)
    k1 = maxDepthIterative(tree.root)
    tree.print_tree(tree.root)


    print(k)
    print(k1)