
'''
Author: Semyon Guretskiy
'''
'''
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values.
(i.e., from left to right, level by level).

Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Solution:
    Uses BFS with a queue to traverse the tree level by level:
    1. Queue stores tuples of (node, level)
    2. Track current level to manage result list structure
    3. Process nodes left to right within each level
    

    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(n)
'''

from typing import Optional, List
from BinaryTree import TreeNode, Tree

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    # Handle empty tree
    if not root:
        return []
    
    # Initialize queue with root node and its level
    queue = [(root, 0)]
    current_level = -1
    result = []
    
    while queue:
        # Get next node and its level
        current_node, level = queue.pop(0)
        
        # Skip None nodes
        if not current_node:
            continue

        # Start new level if needed
        if level > current_level:
            result.append([current_node.val])
            current_level = level
        else:
            # Add to existing level
            result[level].append(current_node.val)
        
        # Add children to queue with next level number
        queue.extend([
            (current_node.left, level + 1),
            (current_node.right, level + 1)
        ])
        
    return result

if __name__ == "__main__":
    # Test case 1: Normal tree
    root = [3,9,20,None,None,15,7]
    root_tree = Tree()
    root_tree.createFromListBFS(root)
    root_tree.print_tree(root_tree.root)
    print(levelOrder(root_tree.root))

    # Test case 2: Single node tree
    root = [1]
    root_tree = Tree()
    root_tree.createFromListBFS(root)
    root_tree.print_tree(root_tree.root)
    print(levelOrder(root_tree.root))
    
    # Test case 3: Empty tree
    root = []
    root_tree = Tree()
    root_tree.createFromListBFS(root)
    root_tree.print_tree(root_tree.root)
    print(levelOrder(root_tree.root))