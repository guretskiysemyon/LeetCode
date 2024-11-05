'''
Author: Semyon Guretskiy
'''

'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Link: https://leetcode.com/problems/add-two-numbers/description/


Solution:
To add two numbers represented as linked lists in reverse order, we iterate through both lists simultaneously, 
adding corresponding digits along with any carry from the previous addition. Since lists might have different lengths, 
we continue with the remaining nodes of the longer list after reaching the end of the shorter one. Finally, if there's 
a remaining carry after processing all nodes, we add an extra node with value 1.
'''

from Linked_List import *

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # Create dummy head to simplify the logic
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    # Process both lists while at least one has nodes
    while l1 or l2 or carry:
        # Get values, using 0 if list is exhausted
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and new carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        # Create new node with calculated digit
        current.next = ListNode(digit)
        current = current.next
        
        # Move to next nodes if available
        if l1: l1 = l1.next  
        if l2: l2 = l2.next  
    
    return dummy.next


if __name__== "__main__":
    l1 = [2,4,3]
    l2 = [5,6,4]

    list1 = LinkedList(l1)
    list2 = LinkedList(l2)

    res = addTwoNumbers(list1.head, list2.head)
    print_list(res) # [7,0,8]

    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]

    list1 = LinkedList(l1)
    list2 = LinkedList(l2)

    res = addTwoNumbers(list1.head, list2.head)
    print_list(res) # [8,9,9,9,0,0,0,1]


    
    
