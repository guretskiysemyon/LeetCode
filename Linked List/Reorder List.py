
'''
Author: Semyon Guretskiy
'''


'''
143. Reorder List
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.


Link: https://claude.ai/chat/b08eb35e-5c3a-4a96-a8bd-cba4d83b3379


Solution:
The reordering process can be broken down into three main steps:
1. Find the middle of the list using the two-pointer technique (fast/slow pointers)
2. Reverse the second half of the list starting from the next to middle node.
3. Merge the first half with the reversed second half alternating between nodes

For even-length lists, we take the first middle node (e.g., for [1,2,3,4], middle is 2).
For odd-length lists, we take the middle node (e.g., for [1,2,3], middle is 2).
'''





from typing import Optional
from Linked_List import * 


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    # Handle edge cases
    if not head or not head.next:
        return head
        
    # Initialize pointers
    previous = None
    current = head
    
    # Traverse and reverse
    while current:
        # Store next node
        next_node = current.next
        # Reverse the link
        current.next = previous
        # Move previous and current forward
        previous = current
        current = next_node
    
    return previous

def reorderList(head: Optional[ListNode]) -> None:

     # Handle edge cases
    if head == None or head.next == None:
        return head
    
    # Step 1: Find the middle of the list
    slow = head
    fast = head.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    

    # Step 2: Reverse the second half
    head_reversed = reverseList(slow.next)
    slow.next = None

     # Step 3: Merge the two halves
    while head_reversed:

        # Save next pointers
        next_original = head.next
        next_reversed = head_reversed.next
       
        # Connect nodes in new order
        head.next = head_reversed
        head_reversed.next = next_original

        # Move pointers forward
        head = next_original
        head_reversed = next_reversed
        
    


if __name__ == "__main__":
    head = [1, 2, 3]
    list_ = LinkedList(head)
    reorderList(list_.head)
    print_list(list_.head)
    head = [1, 2, 3, 4]
    list_ = LinkedList(head)
    reorderList(list_.head)
    print_list(list_.head)
    head = [1, 2, 3 ,4, 5]
    list_ = LinkedList(head)
    reorderList(list_.head)
    print_list(list_.head)
    