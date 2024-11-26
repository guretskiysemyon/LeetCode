'''
Author: Semyon Guretskiy

25. Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example:
    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]

Link: https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Solution:
    The approach uses two main techniques to solve this problem:
    1. Group Detection:
       - Uses a fast pointer to check if there are k nodes ahead
       - Helps determine if we should reverse the current group
       
    2. Group Reversal:
       - Maintains references to previous nodes and group boundaries
       - Reverses nodes within each valid group of k
       - Preserves connections between groups
       - Leaves remaining nodes unchanged if less than k

    Time Complexity: O(n) where n is number of nodes
    Space Complexity: O(1) as we only use pointers
'''

from typing import Optional
from Linked_List import ListNode, LinkedList, print_list

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Create dummy node to handle head changes
    dummy = ListNode(0, head)
    last_tail = dummy  # Keep track of last reversed group's tail
    current = head
    count = 0
    previous = None

    # Move fast pointer k places forward.
    fast = dummy
    while fast and count < k:
        fast = fast.next
        count += 1
    
    if not fast: return head

    count = 0
    while current or count == k:
        if count == k:  # Time to connect reversed group
            # Connect last node of current group to next group
            last_tail.next.next = current
            # Save the original start of group as new tail
            temp = last_tail.next
            # Connect previous group to reversed group
            last_tail.next = previous
            # Update last_tail for next iteration
            last_tail = temp
            
            # If no more full groups, break
            if not fast:
                break
            
            # Reset for next group
            previous = None
            count = 0
        else:
            # Standard linked list reversal
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            count += 1
            
            # Move fast pointer if still valid
            if fast:
                fast = fast.next
    
    return dummy.next

if __name__ == "__main__":
    # Test case: list of 8 nodes with k=3
    # Expected output: Reverse in groups of 3, last 2 nodes unchanged
    head = [1,2,3,4,5,6,7,8]
    k = 3
    lst = LinkedList(head)
    new_head = reverseKGroup(lst.head, k)
    print_list(new_head)