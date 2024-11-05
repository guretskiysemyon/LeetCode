'''
Author: Semyon Guretskiy
'''

'''
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Link: https://leetcode.com/problems/reverse-linked-list/description/


Solution:
To reverse the linked list, we use three pointers: previous, current, and next. We iterate through 
the list and for each node, we store its next node, then point its next pointer to the previous node, 
and finally move the previous and current pointers one step forward. This effectively reverses 
the direction of all links in the list.
'''


from typing import Optional
from Linked_List import ListNode, LinkedList, print_list

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

if __name__ == "__main__":
    head = [1, 2, 3, 5]
    lst = LinkedList(head)
    lst = reverseList(lst.head)
    print_list(lst)