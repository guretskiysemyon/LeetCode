
'''
Author: Semyon Guretskiy
'''

'''
543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Solution:
    1. Recursive DFS:
        For each node, we need to:
        1. Calculate the maximum diameter of left and right subtrees
        2. Calculate the longest path through the current node (using depths of left and right subtrees)
        3. Return both the maximum diameter found and the depth of the current subtree
    2. Iterative DFS:
       - Uses explicit stack to simulate recursion
       - Stores computed results in dictionary
       - Avoids recursion stack overhead

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(h) where h is the height of the tree due to recursion stack
'''

from typing import Optional
from BinaryTree import TreeNode, Tree

def diameterOfBinaryTree(root: Optional[TreeNode], method = "iter") -> int:
    def DFS(root: Optional[TreeNode]) -> tuple[int, int]:
        # Base case: empty node
        if not root:
            return (0, -1)  # Diameter 0, height -1 for null nodes
        
        # Recursively process left and right subtrees
        diameter_left, longest_path_left = DFS(root.left)
        diameter_right, longest_path_right = DFS(root.right)

        # Calculate maximum diameter as the maximum of:
        # 1. Left subtree's diameter
        # 2. Right subtree's diameter
        # 3. Longest path through current node (left_path + right_path + 2 edges)
        maximum = max(
            diameter_left,
            diameter_right,
            longest_path_left + longest_path_right + 2
        )
        
        # Calculate the longest path from current node to any leaf
        longest = max(longest_path_left, longest_path_right) + 1

        return (maximum, longest)
    

    def DFSIterative(root: Optional[TreeNode]) -> tuple[int, int]:
       
        # Handle empty tree case
        if not root:
            return 0
        
        # Initialize stack with root node and dictionary for storing results
        stack = [root]
        # Store results for each node: {node: (diameter, longest_path)}
        # Initialize with None node for leaf node calculations
        nodes_data = {None: (0, -1)}

        while stack:
            current_node = stack[-1]
            
            # Process left subtree if not processed yet
            if current_node.left and current_node.left not in nodes_data:
                stack.append(current_node.left)
                
            # Process right subtree if not processed yet
            elif current_node.right and current_node.right not in nodes_data:
                stack.append(current_node.right)
                
            # If both subtrees are processed, process current node
            else:
                current_node = stack.pop()
                
                # Get results from left and right subtrees
                diameter_left, longest_path_left = nodes_data[current_node.left]
                diameter_right, longest_path_right = nodes_data[current_node.right]
                
                # Store results for current node:
                # 1. Maximum diameter (same calculation as recursive version)
                # 2. Longest path from current node to any leaf
                nodes_data[current_node] = (
                    max(
                        diameter_left,
                        diameter_right,
                        longest_path_left + longest_path_right + 2
                    ),
                    max(longest_path_left, longest_path_right) + 1
                )
                
        # Return only the diameter component from root's results
        return nodes_data[root][0]


    # Choose implementation based on method parameter
    if method == "iter":
        return DFSIterative(root)
    return DFS(root)[0]


if __name__ == "__main__":
    # Test case 1: Empty tree
    root = []
    tree = Tree()
    tree.createFromListBFS(root)
    tree.print_tree(tree.root)
    print(diameterOfBinaryTree(tree.root))

    # Test case 2: Complete binary tree
    root = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    tree = Tree()
    tree.createFromListBFS(root)
    tree.print_tree(tree.root)
    print(diameterOfBinaryTree(tree.root))