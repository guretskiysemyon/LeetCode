'''
Author: Semyon Guretskiy
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    

class Tree:
    def __init__(self) -> None:
        self.root = None

    def createFromListBFS(self, values):

        if not values or values[0] is None:
            return None
            
        # Create root node
        self.root = TreeNode(values[0])
        
        # Use a queue to keep track of nodes that need children
        queue = [self.root]
        i = 1  # Index for values array
        
        # Process each node in the queue
        while queue and i < len(values):
            current = queue.pop(0)
            
            # Add left child if exists
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            
            # Add right child if exists
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        
        return self.root
                

    def print_preorder(self,root):
        if root == None:
            return
        
        print(root.val, end = " ")

        self.print_preorder(root.left)
        self.print_preorder(root.right)


    def print_inorder(self, root):
        if root == None:
            return
        
        self.print_inorder(root.left)
        print(root.val, end = " ")
        self.print_inorder(root.right)


    def print_postorder(self, root):
        if root == None:
            return
        
        self.print_postorder(root.left)
        self.print_postorder(root.right)
        print(root.val, end = " ")


    def print_tree(self,root, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.val))
            self.print_tree(root.left, level + 1, "L--- ")
            self.print_tree(root.right, level + 1, "R--- ")
        


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    tree = Tree()
    tree.createFromListBFS(arr)
    tree.print_tree(tree.root)
    tree.print_inorder(tree.root)
    print("\n")
    tree.print_preorder(tree.root)
    print("\n")
    tree.print_postorder(tree.root)
    print("\n")