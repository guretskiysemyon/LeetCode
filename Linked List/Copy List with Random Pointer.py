'''
Author: Semyon Guretskiy
'''

'''
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of
its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers
in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list,
x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.


Link: https://leetcode.com/problems/copy-list-with-random-pointer/description/


Solution:
There are three main approaches to solve this problem:

1. Dictionary/HashMap Approach (Space: O(n), Time: O(n)):
    - Create a mapping between original nodes and their copies
    - First pass: create all new nodes and store mapping
    - Second pass: connect all pointers using the mapping


2. Space-Optimized Approach (Space: O(1), Time: O(n)):
    - Interweave copied nodes between original nodes
    - Copy random pointers using the interweaved structure
    - Separate the two lists
    - No extra space needed besides the output list


3. DFS/Recursive Approach (Space: O(n), Time: O(n)):
    - Use recursive DFS with memoization
    - Cache created nodes to handle cycles
    - Recursively build next and random connections
'''


from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    




def copyRandomListDictionary(head: Optional[Node]) -> Optional[Node]:
    mapping = {}

    if not head: return None

    # First pass: Create all new nodes
    node = head
    while node:
        mapping[node] = Node(node.val)  # Create copy without connections
        node = node.next

    # Second pass: Connect all pointers
    node = head
    while node:
        # Use mapping to connect both next and random pointers
        mapping[node].next = mapping.get(node.next)    # Handle null next
        mapping[node].random = mapping.get(node.random) # Handle null random
        node = node.next

    return mapping[head]


def copyRandomListConstantSpace(head: Optional[Node]) -> Optional[Node]:
    # Step 1: Create interleaved list
    # Original: A -> B -> C
    # Becomes:  A -> A' -> B -> B' -> C -> C'
    l1_node = head
    while l1_node:
        l2_node = Node(l1_node.val)
        l2_node.next = l1_node.next
        l1_node.next = l2_node
        l1_node = l2_node.next

    # Step 2: Copy random pointers using interleaved structure
    l1_node = head
    while l1_node:
        l2_node = l1_node.next
        if l1_node.random:
            l2_node.random = l1_node.random.next  # Point to copy of random node
        else:
            l2_node.random = None
        l1_node = l2_node.next

    # Step 3: Separate the two lists
    new_head = head.next
    l1_node = head
    while l1_node:
        l2_node = l1_node.next
        l1_node.next = l2_node.next  # Restore original list
        if l1_node.next:
            l2_node.next = l1_node.next.next  # Connect copied list
        else:
            l2_node.next = None
        l1_node = l1_node.next

    return new_head



def copyRandomListDFS(head: Optional[Node]) -> Optional[Node]:
    mapping = {}
    def dfs_search(node):
        if not node:
            return None
            
        # If node already copied, return cached copy
        copied_node = mapping.get(node)
        if copied_node:
            return copied_node
        
        # Create new node and cache it
        new_node = Node(node.val)
        mapping[node] = new_node
        
        # Recursively copy next and random connections
        new_node.next = dfs_search(node.next)
        new_node.random = dfs_search(node.random)
        
        return new_node
        
    return dfs_search(head)
        



# Create Linked List using List
def create_list(head):
    node_list = []
    n = len(head)

    if n == 0: return None

    prev_node = Node(head[0][0])
    node_list.append(prev_node)
    
    for i in range(1, n):
        node = Node(head[i][0])
        prev_node.next = node
        node_list.append(node)
        prev_node = node
    
    prev_node.next = None

    for i in range(n):
        value = head[i][1]
        if value != None:
            node_list[i].random = node_list[value]
        else:
            node_list[i].random = None
    
    return node_list[0]

    
# Check if two list are equal by comapring value, next value and random value. Can be not right for some case.
def test(head):
    new_head = create_list(head)

    copied_head = copyRandomListConstantSpace(new_head)

    string1 = ""
    node = new_head
    while node:
        string1 += f"Val: {node.val}\n"
        if node.next != None:
            string1 += f"Next Val: {node.next.val}\n"
        else:
            string1 += f"Next Val: {None}\n"
        
        if node.random != None:
            string1 += f"Random Val: {node.random.val}\n"
        else:
             string1 += f"Random Val: {None}\n"

        
        node = node.next
    

    string2 = ""
    node = copied_head
    while node:
        string2 += f"Val: {node.val}\n"
        if node.next != None:
            string2 += f"Next Val: {node.next.val}\n"
        else:
            string2 += f"Next Val: {None}\n"
        
        if node.random != None:
            string2 += f"Random Val: {node.random.val}\n"
        else:
             string2 += f"Random Val: {None}\n"

        
        node = node.next

    
    print(string1 == string2)



if __name__ == "__main__":
    head = [[7, None],[13,0],[11,4],[10,2],[1,0]]
    test(head)

    head = [[1,1],[2,1]]
    test(head)


    head = [[3,None],[3,0],[3,None]]
    test(head)