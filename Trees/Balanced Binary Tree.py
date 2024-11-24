
'''
Author: Semyon Guretskiy
'''


'''
110. Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees
of every node never differs by more than one.

Link: https://leetcode.com/problems/balanced-binary-tree/description/

Solution:
The solution uses DFS post-order traversal with two different approaches:

1. Recursive Approach:
   - Uses natural recursion with DFS post-order traversal
   - Returns height of subtree if balanced, -1 if unbalanced
   - Checks balance condition at each node
   - Returns early if imbalance is detected

2. Iterative Approach:
   - Simulates recursion using stack for DFS post-order traversal
   - Uses dictionary to store heights of processed nodes
   - Returns False as soon as imbalance is detected
   - Returns True if entire tree is processed without finding imbalance

Time Complexity: O(n) where n is number of nodes
Space Complexity: O(n) where h is height of the tree
'''

from typing import Optional
from BinaryTree import TreeNode, Tree

def isBalancedRecursive(root: Optional[TreeNode]) -> bool:
    def isBalancedDFS(root: Optional[TreeNode]) -> int:
        # Base case: empty node has height 0
        if not root: 
            return 0

        # Get heights of left and right subtrees
        left_depth = isBalancedDFS(root.left)
        right_depth = isBalancedDFS(root.right)

        # Return -1 if subtree is unbalanced or current node creates imbalance
        if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
            return -1
        
        # Return height of current subtree
        return max(left_depth, right_depth) + 1
    
    # Tree is balanced if DFS didn't return -1
    return isBalancedDFS(root) >= 0

def isBalanced(root: Optional[TreeNode]) -> bool:
    # Handle empty tree case
    if not root:
        return 0
    
    # Initialize stack for DFS traversal
    stack = [root]
    
    # Dictionary to store heights of processed nodes
    nodes_data = {None: 0}  # Empty node has height 0

    while stack:
        current_node = stack[-1]
        
        # Process left subtree if not visited
        if current_node.left and current_node.left not in nodes_data:
            stack.append(current_node.left)
            
        # Process right subtree if not visited
        elif current_node.right and current_node.right not in nodes_data:
            stack.append(current_node.right)
            
        # Process current node if both children are visited
        else:
            current_node = stack.pop()
            
            # Get heights of left and right subtrees
            depth_left = nodes_data[current_node.left]
            depth_right = nodes_data[current_node.right]
            
            # Return False if imbalance detected
            if depth_left == -1 or depth_right == -1 or abs(depth_left - depth_right) > 1:
                return False
            
            # Store height of current subtree
            nodes_data[current_node] = max(depth_left, depth_right) + 1
            
    return True

if __name__ == "__main__":
    # Test case 1: Balanced tree
    root = [3,9,20, None, None ,15,7]
    tree = Tree()
    tree.createFromListBFS(root)
    k = isBalanced(tree.root)
    tree.print_tree(tree.root)
    print(k)
    
    # Test case 2: Unbalanced tree
    root = [1,2,2,3,3,None,None,4,4]
    tree = Tree()
    tree.createFromListBFS(root)
    k = isBalanced(tree.root)
    tree.print_tree(tree.root)
    print(k)