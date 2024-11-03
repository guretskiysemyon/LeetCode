

'''981. Time Based Key-Value Store

Design a time-based key-value data structure that can store multiple values for
the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key with the value value
at the given time timestamp.
- String get(String key, int timestamp) Returns a value such that set was called previously,
with timestamp_prev <= timestamp. If there are multiple such values, it returns the value
associated with the largest timestamp_prev. If there are no values, it returns "".



Link: https://leetcode.com/problems/time-based-key-value-store/description/



Solution:
Use binary search with and it there is no such timestamp return a previous one.
'''

class TimeMap:
    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
            
        timestamps = self.store[key]
        
        # Handle edge cases
        if timestamps[0][0] > timestamp:
            return ""
        if timestamps[-1][0] <= timestamp:
            return timestamps[-1][1]
            
        # Binary search
        left, right = 0, len(timestamps) - 1
        
        # Search for the largest timestamp <= target
        while left < right:
            mid = (left + right + 1) // 2
            if timestamps[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1
        
        # If there is no such timestamp.
        return timestamps[left][1]








if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("love","high",10)
    timeMap.set("love","low",20)
    print(timeMap.get("love", 5))
    # print(timeMap.get("foo", 3))
    # timeMap.set("foo", "bar2", 4)
    # print(timeMap.get("foo", 4))
    # print(timeMap.get("foo", 5))         