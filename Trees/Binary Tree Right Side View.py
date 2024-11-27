'''
Author: Semyon Guretskiy
'''

'''
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Link: https://leetcode.com/problems/binary-tree-right-side-view/description/

Solution:
    Uses level-order traversal (BFS) to find rightmost nodes at each level.
    Two implementations provided:

    1. Using level order traversal:
       - Get all nodes at each level
       - Take rightmost node from each level
       
    2. Direct right side view (optimized):
       - Track level transitions
       - Only store rightmost node at each level
       - Add only non-null children to queue
    
    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(max(w,h)) where w is maximum width of tree and h is maximum height of the tree
'''

from typing import Optional, List
from BinaryTree import TreeNode, Tree


def rightSideView(root: Optional[TreeNode]) -> List[int]:
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
            if current_node.left:
                queue.append((current_node.left, level + 1))
            if current_node.right:
                queue.append((current_node.right, level + 1))

            
        return result

    levels_order = levelOrder(root)
    for i, x in enumerate(levels_order):
        levels_order[i] = x[-1]    
    return levels_order




def rightSideView(root: Optional[TreeNode]) -> List[int]:
    # Empty tree case
    if not root:
        return []
    
    # Queue stores (node, level) pairs
    queue = [(root, 0)]
    result = []
    
    while queue:
        current_node, level = queue.pop(0)
        
        if not current_node:
            continue

        # Add node if it's last in level or queue is empty
        if (queue and queue[0][1] > level) or (not queue):
            result.append(current_node.val)
        
        # Add non-null children only
        if current_node.left:
            queue.append((current_node.left, level + 1))
        if current_node.right:
            queue.append((current_node.right, level + 1))
    
    return result





if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1],                            # Single node
        [],                             # Empty tree
        [1,2,3,None,5,None,4],         # Normal tree
        [1,2,3,4,None,None,None,5]     # Deep left subtree
    ]
    
    for root in test_cases:
        root_tree = Tree()
        root_tree.createFromListBFS(root)
        root_tree.print_tree(root_tree.root)
        print(rightSideView(root_tree.root))
