'''
Author: Semyon Guretskiy
'''
'''
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Link: https://leetcode.com/problems/same-tree/description/

Solution:
    Two approaches are implemented to solve this problem:

    1. Recursive Approach:
       - Uses DFS to traverse both trees simultaneously
       - Compares corresponding nodes at each step
       - Returns false as soon as a mismatch is found
       - Base cases handle null nodes

    2. Iterative Approach:
       - Uses BFS with two queues to traverse trees level by level
       - Compares corresponding nodes at each level
       - Returns false on first mismatch
       - Handles null nodes explicitly

    Time Complexity: O(min(n,m)) where n and m are numbers of nodes in trees
    Space Complexity: O(min(h1,h2)) for recursive where h1,h2 are heights
                      O(w) for iterative where w is maximum width of either tree
'''

from typing import Optional
from BinaryTree import TreeNode, Tree

def isSameTreeRecursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # If both nodes are None, trees are identical
    if p == q:
        return True
    
    # If only one node is None, trees are different
    if not p or not q:
        return False
    
    # If values are different, trees are different
    if p.val != q.val:
        return False
    
    # Recursively check left and right subtrees
    return isSameTreeRecursive(p.left, q.left) and isSameTreeRecursive(p.right, q.right)
    

def isSameTreeIterative(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Initialize queues for BFS traversal
    p_stack = [p]
    q_stack = [q]

    while p_stack and q_stack:
        # Get next nodes from both queues
        curr_p = p_stack.pop(0)
        curr_q = q_stack.pop(0)

        # Skip if both nodes are None
        if not curr_p and not curr_q:
            continue

        # If only one is None, trees are different
        if not curr_p or not curr_q:
            return False
        
        # If values differ, trees are different
        if curr_p.val != curr_q.val:
            return False
        
        # Add children to queues for processing
        p_stack.append(curr_p.left)
        p_stack.append(curr_p.right)
        q_stack.append(curr_q.left)
        q_stack.append(curr_q.right)
    
    # Check if both queues are empty (trees have same structure)
    if p_stack != [] or q_stack != []:
        return False
    
    return True

if __name__ == "__main__":
    # Test case: Two identical trees
    p = [1,2,3]
    q = [1,2,3]
    
    # Create and print first tree
    tree_p = Tree()
    tree_p.createFromListBFS(p)
    tree_p.print_tree(tree_p.root)

    # Create and print second tree
    tree_q = Tree()
    tree_q.createFromListBFS(q)
    tree_q.print_tree(tree_q.root)

    # Test both implementations
    k = isSameTreeRecursive(tree_p.root, tree_q.root)
    print(k)
    k = isSameTreeIterative(tree_p.root, tree_q.root)
    print(k)