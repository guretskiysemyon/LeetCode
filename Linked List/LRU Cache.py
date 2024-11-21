

'''
Author: Semyon Guretskiy
'''

'''
146. LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
    Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity
    from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Link: https://leetcode.com/problems/lru-cache/description/


Solution:
An LRU cache is implemented using a dictionary and a doubly linked list.

'''
from Linked_List import *

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # Create dummy head and tail nodes to simplify insertion/deletion
        self.head = ListNodeTwoDirectrion(None)
        self.tail = ListNodeTwoDirectrion(None)
        # Connect head and tail
        self.head.next = self.tail
        self.tail.previous = self.head
        
        # Dictionary to store key -> [value, node] mappings
        self.cache_map = {}
        pass
    

    def _remove(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def _put_first(self, node):
        # Connect node to the node after head
        node.next = self.head.next
        self.head.next.prev = node
        # Connect head to node
        self.head.next = node
        node.prev = self.head


    def get(self, key: int) -> int:
        data = self.cache_map.get(key)
        if not data: return -1
        
        # Update access order by moving node to front
        self._remove(data[1])
        self._put_first(data[1])

        return data[0]



    def put(self, key: int, value: int) -> None:
        data = self.cache_map.get(key)

        if data: # Key exists, update value and move to front
            data[0] = value
            self._remove(data[1])
            self._put_first(data[1])
            return

        # Create new node and add to cache
        new_node = ListNodeTwoDirectrion(key)
        self.cache_map[key] = [value, new_node]
        self._put_first(new_node)
        
        # If over capacity, remove least recently used (node before tail)
        if len(self.cache_map) > self.capacity:
            self.cache_map.pop(self.tail.prev.val)
            self._remove(self.tail.prev)

        


            






if __name__ == "__main__":

    cache = LRUCache(3)
    cache.put(1, 1)
    print_list(cache.head)
    cache.put(2, 2)
    print_list(cache.head)
    cache.put(3, 3)
    print_list(cache.head)
    cache.get(1)
    print_list(cache.head)
    cache.get(2)  
    print_list(cache.head)
    cache.put(4, 4)
    print_list(cache.head)
    cache.get(1)
    print_list(cache.head)  
    cache.get(3)
    print_list(cache.head)  
    cache.get(4)
    print_list(cache.head)


    print("\n\n")
    ["LRUCache","put","get","put","get","get"]
    [[1],[2,1],[2],[3,2],[2],[3]]

    cache = LRUCache(1)
    cache.put(2, 1)
    print_list(cache.head)
    cache.get(2)
    print_list(cache.head)
    cache.put(3, 2)
    print_list(cache.head)
    cache.get(2)
    print_list(cache.head)
    cache.get(3)

    print("\n\n")
    ["LRUCache","put","put","get","put","put","get"]
    [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    cache = LRUCache(2)
    cache.put(2, 1)
    print_list(cache.head)
    cache.put(2, 2)
    print_list(cache.head)
    cache.get(2)
    print_list(cache.head)
    cache.put(1, 1)
    print_list(cache.head)
    cache.put(4, 1)
    print_list(cache.head)
    cache.get(2)

