'''
Author: Semyon Guretskiy
'''


'''
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list
and return its head.

Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/




Solution:
We create two pointers - right and left. Firstly we move right pointer n times toward the tail,
and then we start to move them together (i.e. left = left.next, right = right.next).
When we reach the point that right is None then we reached the end of the list, and now we know that
left one is nth element from the end of the list and we can remove it.

'''



from Linked_List import *


def removeNthFromEnd(head, n):
        temp = ListNode(0, head)
        left = temp
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right is not None:
            left = left.next
            right = right.next

        left.next = left.next.next
        return temp.next





if __name__ == "__main__":
    arr_val = [1,2,3,4,5]
    #n = 2

    print(arr_val)

    for i in range(1, len(arr_val)+1):
        print(i, end = ": ")
        list_ = LinkedList(arr_val)
        update_list = removeNthFromEnd(list_.head, i)
        print_list(update_list)
