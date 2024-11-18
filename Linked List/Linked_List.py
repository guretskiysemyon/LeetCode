'''
Author: Semyon Guretskiy
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class ListNodeTwoDirectrion(object):
    def __init__(self, val=0, next=None, previous = None):
        self.val = val
        self.next = next
        self.prev = previous



class LinkedList(object):
    def __init__(self, arr):
        n = len(arr)
        if len(arr) == 0:
            self.head = None

        self.head = ListNode(arr[0])
        last = self.head
        for i in range(1, n):
            new_node = ListNode(arr[i])
            last.next = new_node
            last = new_node


    
    def add(self, val):
        new_node = ListNode(val)
        next_node = self.head.next
        while next_node is not None:
            next_node = next_node.next
        next_node.next = new_node


def print_list(head):
    print("[", end = " ")
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print("]")