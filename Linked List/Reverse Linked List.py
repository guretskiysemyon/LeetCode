

from typing import Optional
from Linked_List import ListNode, List, print_list

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    first = None
    curr = head
    while curr is not None:
        nxt = curr.next
        curr.next = first
        first = curr
        curr = nxt
    return first


if __name__ == "__main__":
    head = [1,2]
    lst = List(head)
    lst = reverseList(lst.first)
    print_list(lst)