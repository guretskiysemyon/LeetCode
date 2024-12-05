
'''
Author: Semyon Guretskiy
'''


'''
572. Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is a subtree
of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this
node's descendants. The tree tree could also be considered as a subtree of itself.

Link: https://leetcode.com/problems/subtree-of-another-tree/description/

Solution:
    Two implementations are provided, both using a similar approach but with different methods 
    to check if trees are identical:

    1. Using recursive tree comparison:
       - Traverse main tree recursively
       - When values match, check if subtrees are identical using recursive comparison
       - Continue traversal if match not found
       
    2. Using iterative tree comparison:
       - Traverse main tree recursively
       - When values match, check if subtrees are identical using BFS traversal
       - Continue traversal if match not found

    Both approaches work by:
    1. Finding nodes in the main tree that match the root of subtree
    2. When match found, comparing entire subtrees for equality
    3. If comparison fails, continuing to search in remaining nodes

    Time Complexity: O(m*n) where m and n are numbers of nodes in trees
    Space Complexity: O(h) where h is height of larger tree
'''

from typing import Optional
from BinaryTree import TreeNode, Tree

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSameTreeRecursive(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both nodes are None
        if p == q:
            return True
        
        # If only one node is None
        if not p or not q:
            return False
        
        # Compare current nodes
        if p.val != q.val:
            return False
        
        # Compare both subtrees
        return isSameTreeRecursive(p.left, q.left) and isSameTreeRecursive(p.right, q.right)
    
    # Base cases for subtree check
    if root == subRoot:
        return True
    
    if not root or not subRoot:
        return False
    
    # If current nodes match, check if trees are identical
    if root.val == subRoot.val:   
        left = isSameTreeRecursive(root.left, subRoot.left)
        right = isSameTreeRecursive(root.right, subRoot.right)
        
        if left and right:
            return True
    
    # Continue search in left and right subtrees
    return isSubtree(root.right, subRoot) or isSubtree(root.left, subRoot)
    

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    def isSameTreeIterative(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Use queues for level-order traversal
        p_stack = [p]
        q_stack = [q]

        while p_stack and q_stack:
            curr_p = p_stack.pop(0)
            curr_q = q_stack.pop(0)

            # Both None nodes
            if not curr_p and not curr_q:
                continue

            # One None, one not None
            if not curr_p or not curr_q:
                return False
            
            # Different values
            if curr_p.val != curr_q.val:
                return False
            
            # Add children for comparison
            p_stack.append(curr_p.left)
            p_stack.append(curr_p.right)
            q_stack.append(curr_q.left)
            q_stack.append(curr_q.right)
        
        # Check if both trees were fully traversed
        return not p_stack and not q_stack
    
    # Base cases for subtree check
    if root == subRoot:
        return True
    
    if not root or not subRoot:
        return False
    
    # If values match, check if trees are identical
    if root.val == subRoot.val:   
        left = isSameTreeIterative(root.left, subRoot.left)
        right = isSameTreeIterative(root.right, subRoot.right)
        
        if left and right:
            return True
    
    # Continue search in subtrees
    return isSubtree(root.right, subRoot) or isSubtree(root.left, subRoot)





if __name__ == "__main__":
    # Test case with subtree present
    root = [3,5,4,7,8,1,2]
    subRoot = [4,1,2]
    
    # Create and display main tree
    root_tree = Tree()
    root_tree.createFromListBFS(root)
    root_tree.print_tree(root_tree.root)

    # Create and display subtree to find
    subRoot_tree = Tree()
    subRoot_tree.createFromListBFS(subRoot)
    subRoot_tree.print_tree(subRoot_tree.root)

    # Check if subtree exists
    k = isSubtree(root_tree.root, subRoot_tree.root)
    print(k)