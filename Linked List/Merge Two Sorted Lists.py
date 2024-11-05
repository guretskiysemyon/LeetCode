'''
Author: Semyon Guretskiy
'''


'''
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing
together the nodes of the first two lists.

Return the head of the merged linked list.


Link: https://leetcode.com/problems/merge-two-sorted-lists/description/

'''


from Linked_List import *


def mergeTwoLists(list1, list2):
        new_head = ListNode()
        cur = new_head
        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2

        return new_head.next



if __name__ == "__main__":
    list_arr1 = [1,2,4]
    list_arr2 = [1,3,4]
    
    list1 = LinkedList(list_arr1)
    list2 = LinkedList(list_arr2)

    merge_list = mergeTwoLists(list1.head, list2.head)
    print_list(merge_list)
