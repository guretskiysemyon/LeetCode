'''
Author: Semyon Guretskiy
'''
'''
23. Merge k Sorted Lists
Hard
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Solution:
    Three implementations provided with different time/space tradeoffs:

    1. Naive Approach:
       - Find minimum value across all list heads
       - Add to result and advance pointer
       - Time: O(kN) where k is number of lists, N total nodes
       
    2. Divide and Conquer:
       - Merge pairs of lists recursively
       - Reduces comparisons needed
       - Time: O(N log k)
       
    3. Heap-based:
       - Use min-heap to track smallest values
       - Time: O(N log k)
'''

from math import inf
from Linked_List import *
from typing import Optional, List

def mergeKListsNaive(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Handle empty input
    if not lists:
        return None
        
    k = len(lists)
    result = ListNode(0)
    current = result
    
    while True:
        # Find minimum value among list heads
        minimum = ListNode(inf)
        minimum_index = -1
        go_on = False
        
        # Check all list heads
        for i in range(k):
            if lists[i] and lists[i].val < minimum.val:
                minimum = lists[i]
                minimum_index = i
                go_on = True
                
        if not go_on:
            break
            
        # Add minimum to result and advance pointer
        current.next = minimum
        current = minimum
        lists[minimum_index] = lists[minimum_index].next
    
    return result.next

def mergeKListsDevideConquer(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def mergeTwoLists(list1, list2):
        # Merge two sorted lists
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2
        return dummy.next
    
    if not lists:
        return None
    
    # Merge pairs until single list remains
    while len(lists) > 1:
        merged = []
        
        for i in range(0, len(lists), 2):
            if i + 1 == len(lists):
                merged.append(lists[i])
            else:
                merged.append(mergeTwoLists(lists[i], lists[i+1]))
                
        lists = merged

    return lists[0]
    
class NodeWrapper:
    def __init__(self, node) -> None:
        self.node = node
    def __lt__(self, other):
        return self.node.val < other.node.val

def mergeKListsHeap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    if not lists:
        return None
    
    import heapq
    
    # Initialize result list
    result = ListNode(0)
    current = result
    heap = []
    
    # Add all nodes to heap
    for l in lists:
        node = l
        while node:
            heapq.heappush(heap, NodeWrapper(node))
            node = node.next
    
    # Build result from heap
    while heap:
        minimum = heapq.heappop(heap).node
        current.next = minimum
        current = minimum
    
    current.next = None
    return result.next

if __name__ == "__main__":
    # Test case 1: Three sorted lists
    lists = [[1,4,5],[1,3,4],[2,6]]
    list_of_lists = [LinkedList(l).head for l in lists]
    res = mergeKListsHeap(list_of_lists)
    print_list(res)

    # Test case 2: Two sorted lists with duplicates
    lists = [[1,2,2],[1,1,2]]
    list_of_lists = [LinkedList(l).head for l in lists]
    res = mergeKListsHeap(list_of_lists)
    print_list(res)