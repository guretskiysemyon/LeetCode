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

    def createFromListBFS(self, arr):
        lenght = len(arr)
        queue = []
        if lenght == 0:
            return self.root
        
        arr.append(None)
        self.root = TreeNode(arr[0])
        queue.append(self.root)
    
        i = 1
        while i < lenght:
            curr = queue.pop(0)
            left_node = TreeNode(arr[i])
            right_node = TreeNode(arr[i+1])
            queue.append(left_node)
            queue.append(right_node)
            curr.left = left_node
            curr.right = right_node
            i += 2
        
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