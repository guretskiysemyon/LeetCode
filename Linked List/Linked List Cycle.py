'''
Author: Semyon Guretskiy
'''

'''
141. Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Link: https://leetcode.com/problems/linked-list-cycle/description/

Solution:
To detect a cycle in a linked list, we use the Floyd's Cycle-Finding Algorithm (also known as the "tortoise and hare" algorithm). 
We use two pointers moving at different speeds: 'slow' moves one step at a time while 'fast' moves two steps. 
If there's a cycle, the fast pointer will eventually meet the slow pointer inside the cycle. 
If there's no cycle, the fast pointer will reach the end of the list.

'''



def hasCycle(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


